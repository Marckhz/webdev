from faker import Faker

from models.entities import Skill, User


def init(db, config,):
    fake = Faker()
    users = [User(name=fake.name()) for _ in range(10)]
    for u in users:
        db.session.add(u)
    
    db.session.commit()

