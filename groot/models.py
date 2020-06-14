from datetime import datetime
from groot import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


policies_users = db.Table('policies_users',
                          db.Column('user_id', db.Integer,
                                    db.ForeignKey('users.id')),
                          db.Column('policy_id', db.Integer, db.ForeignKey('policies.id')))

sensors_policies = db.Table('sensors_policies',
                            db.Column('policy_id', db.Integer,
                                      db.ForeignKey('policies.id')),
                            db.Column('sensor_id', db.Integer, db.ForeignKey('sensors.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False, unique=False)
    last_name = db.Column(db.String(30), nullable=False, unique=False)
    nick_name = db.Column(db.String(30), nullable=False, unique=False)
    image_file = db.Column(db.String(50), nullable=False,
                           default='default_profile.png')
    password = db.Column(db.String(200), nullable=False, unique=False)
    policies_wrote = db.relationship("Policy", backref="owner", lazy=True)
    comments_wrote = db.relationship("Comment", backref="author", lazy=True)
    policies_used = db.relationship("Policy", secondary=policies_users,
                                    backref=db.backref('policies_used', lazy='dynamic'))

    def __repr__(self):
        return {'email': self.email, 'first_name': self.first_name, 'last_name': self.last_name,
                'nick_name': self.nick_name, 'password': self.password}


class Policy(db.Model):
    __tablename__ = 'policies'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False,
                          unique=False, default=False)
    policy_name = db.Column(db.String(20), nullable=False, unique=True)
    plant_type = db.Column(db.String(30), nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    amount_light = db.Column(db.Integer, nullable=False)
    irregation_frequency = db.Column(db.Integer, nullable=False)
    irregation_amount = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    writer = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    policy_users = db.relationship("User", backref="used_by", lazy=True)
    policy_comments = db.relationship("Comment", backref="wrote_by", lazy=True)
    policy_sensors = db.relationship("Sensor", secondary=sensors_policies,
                                     backref=db.backref('policy_sensors', lazy='dynamic'))

    def __repr__(self):
        return {'id': self.id, 'policy_name': self.policy_name, 'plant_type': self.plant_type,
                'humidity': self.humidity, 'amount_light': self.amount_light,
                'irregation_frequency': self.irregation_frequency,
                'irregation_amount': self.irregation_amount, 'date_created': self.date_created}


class Sensor(db.Model):
    __tablename__ = 'sensors'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    type = db.Column(db.String(30), nullable=False, unique=False)
    is_active = db.Column(db.Boolean, nullable=False, unique=False)

    def __repr__(self):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'is_active': self.is_active}


class Comment(db.Model):
    __tablename__ = 'comments'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=False)
    content = db.Column(db.Text, nullable=False, unique=False)
    date_posted = db.Column(db.String(30), nullable=False, unique=True,
                            default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    writer = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey(
        'policies.id'), nullable=False)

    def __repr__(self):
        return {'id': self.id, 'title': self.title, 'content': self.content, 'date_posted': self.date_posted}
