from app import create_app, db

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    try:
        with open("app/instance/BaseD.db") as base:    
            app.run(debug=True)
    except FileNotFoundError:
        init_db()
        app.run(debug=True)
