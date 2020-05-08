from groot import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User: {}>'.format(self.username)