from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    location = db.Column(db.String(64), index=True)
    address = db.Column(db.String(120), index=True)
    apikey = db.Column(db.String(64), index=True, unique=True)



    def __repr__(self):
        return '<User %r>' % self.name
