from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Guardar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ese nombre de usuario ya está en uso. Por favor elige otro.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Ese correo electrónico ya está en uso. Por favor elige otro.')

class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recordar')
    submit = SubmitField('Iniciar sesión')

class ProductForm(FlaskForm):
    name = StringField('Nombre',validators=[DataRequired()])
    description = StringField('Descripción',validators=[DataRequired()])
    price = FloatField('Precio',validators=[DataRequired()])
    path_image = StringField('Dirección de la imagen', validators=[DataRequired()])
    submit = SubmitField('Cargar producto')

class OfferForm(FlaskForm):
    id_product = IntegerField('Id del producto',validators=[DataRequired()])
    offer_price = FloatField('Precio',validators=[DataRequired()])
    offer_description = StringField('Descripición',validators={DataRequired()})
    offer_open = DateField('Fecha de inicio', validators=[DataRequired()])
    offer_end = DateField('Fecha de cierre', validators=[DataRequired()])
    offer_days = StringField('Dias de la semana', validators=[DataRequired()])

class UserEditForm(FlaskForm):
    id = IntegerField('ID del usuario',validators=[],default=None)
    username = StringField('Nombre de usuario', validators=[Length(min=2, max=20)],default=None)
    email = StringField('Correo electrónico', validators=[Email()],default=None)
    selector = SelectField('Seleccione a través de que dato buscará el usuario',choices=[('id','ID'),('username','Nombre de usuario'),('email','Email')], id="selector")
    submit = SubmitField('Buscar usuario')

    # def validate_id(self,id):
    #     user = User.query.filter_by(id=id).first()
    #     if not user:
    #         raise ValidationError('Ese usuario no existe')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('Ese nombre de usuario no está registrado')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Ese correo electrónico no está registrado')
