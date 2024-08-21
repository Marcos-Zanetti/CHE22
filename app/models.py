from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
   
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    path_image = db.Column(db.String(200), default=False)

    def __repr__(self):
        return f"Products('{self.name}', '{self.description}', '{self.price}', '{self.pathImage}')"


class Offers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProduct = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    products = db.relationship('Products', backref = ('Offers'))
    offerPrice = db.Column(db.Float, nullable=False)
    offerDescription = db.Column(db.String(200), unique=True, nullable=False)
    offerOpen = db.Column(db.Date, nullable=False)
    offerEnd = db.Column(db.Date, nullable=False)
    offerDay = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Offers('{self.offerPrice}', '{self.offerDescription}', '{self.offerOpen}', '{self.offerEnd}', '{self.offerDay}')"