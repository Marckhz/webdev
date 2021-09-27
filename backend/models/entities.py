from models import db

skills = db.Table('user_skill_relation',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')))


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    subscriptions = db.relationship('Skill', secondary=skills,
                    backref=db.backref('subscribers', lazy='dynamic'))

    def __repr__(self):
        return "<User %r>" % self.name


class Skill(db.Model):
    __tablename__ = "skill"
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'Skill {self.skill}'