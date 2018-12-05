from main import db

class User(db.Model):
    username = db.Column(db.String(120), primary_key=True,
                         unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profilePic = db.Column(db.String, unique=True, nullable=True)
    receipts = db.Column(db.String, nullable=True)
    creditCardNumber = db.Column(db.String(16), unique=True, nullable=True)
    creditCardExpiration = db.Column(db.String, nullable=True)
    creditCardCVC = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
