from flask import render_template, url_for, flash, redirect, session, request
from app import db
from app.models import User, Products
from app.forms import RegistrationForm, LoginForm, ProductForm, UserEditForm

def init_routes(app):

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('¡Tu cuenta ha sido creada!', 'success')
            session['user_id'] = user.id
            return redirect(url_for('index'))
        return render_template('register.html', title='Registro', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.password == form.password.data:
                session['user_id'] = user.id
                flash('¡Inicio de sesión exitoso!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Inicio de sesión fallido. Por favor, verifica tu correo y contraseña.', 'danger')
        return render_template('login.html', title='Iniciar sesión', form=form)

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        flash('Has cerrado sesión.', 'info')
        return redirect(url_for('index'))
    
    @app.route('/admin_product', methods=['GET','POST'])
    def carga_producto():
        form = ProductForm()
        if form.validate_on_submit():
            product = Products(name=form.name.data, description=form.description.data, price=form.price.data, path_image=form.path_image.data)
            db.session.add(product)
            db.session.commit()
            flash('El producto a sido agregado','success')
            return redirect(url_for('productos'))
        return render_template('admin_product.html', form=form)
    
    @app.route('/admin')
    def admin():
        if session['user_id']:
            user = User.query.filter_by(id=session['user_id']).first()
            db.session.delete(user)
            db.session.commit()
            user_admin = User(username=user.username,email=user.email,password=user.password,is_admin=True)
            db.session.add(user_admin)
            db.session.commit()
        return redirect('index')

    @app.route('/table_product')
    def productos():
        registros = []
        for registro in db.session.query(Products):
            registros.append(registro.name)
        return render_template('table_product.html',registros=registros)
    
    @app.route('/user_edit',methods=["GET","POST"])
    def user_edit():
        form = UserEditForm()
        if form.id.data != None or form.username.data != None or form.email.data != None:
            idData = request.form["id"]
            nameData = request.form["username"]
            mailData = request.form["email"]
            if idData != None:
                # flash(f'ID: {idData}','success')
                user = User.query.filter_by(id=idData).first()
                flash(user,'success')
            elif nameData != None:
                # flash(f'Nombre de usuario: {nameData}','success')
                user = User.query.filter_by(username=f"%{nameData}%")
                flash(user,'success')
            elif mailData != None:
                # flash(f'Email: {mailData}','success')
                user = User.query.filter_by(email=f"%{mailData}%")
                flash(user,'success')
        else:
            flash(f'{form.id.data},{form.username.data},{form.email.data}','danger')
        return render_template('user_edit.html',form=form)