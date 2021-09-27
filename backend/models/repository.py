import logging
from typing import List

from sqlalchemy.exc import IntegrityError

from dto.requests_payload import SkillsDTO, UserDTO, UserSkillDTO
from models import db
from models.entities import Skill, User

logger = logging.getLogger(__name__)


def save_user(user_dto: UserDTO):
    user = user_dto.to_orm()
    db.session.add(user)
    logger.info(f'user object {user}')
    try:
        db.session.commit()
        logger.info(f'New user created {user_dto.name} was succesfully saved.')
    except IntegrityError as e:
        logger.error(f'Failed to create new user got {str(e)[:90]}')
        raise SaveEntityException(f'Failed to save user: {user_dto.name}')


def get_all_users():
    users = db.session.query(User).all()
    return users


def get_user_by_id(user_id: int) -> User:
    return db.session.query(User).filter(User.id == user_id).first()


def delete_users():
    users = db.session.query(User).all()
    [u.subscriptions.clear() for u in users]
    db.session.query(User).delete()
    db.session.commit()


def save_skill(skill_dto: SkillsDTO):
    skill = skill_dto.to_orm()
    db.session.add(skill)
    logger.info(f'skill object {skill}')
    try:
        db.session.commit()
        logger.info(f'New skill created {skill_dto.skill} was successfuly saved.')
        return skill
    except IntegrityError as e:
        logger.error(f'Failed to create new skill {str(e)[:90]}')
        raise SaveEntityException(f'Failed to save skill: {skill_dto.skill}')


def filter_skill_by_name(skill_dto: SkillsDTO) -> Skill:
    return db.session.query(Skill).filter(Skill.skill == skill_dto.skill).first()


def filter_skill_by_id(skill_dto: SkillsDTO)->Skill:
    return db.session.query(Skill).filter(Skill.id == skill_dto.id).first()


def save_user_skill(user_skill: UserSkillDTO):
    skill = user_skill.skill
    user_id = user_skill.user.id
    skill_obj = filter_skill_by_name(skill)
    if not skill_obj:
        skill_obj = save_skill(skill)
    try:
        user = get_user_by_id(user_id)
        user.subscriptions.append(skill_obj)
        db.session.commit()
    except IntegrityError as e:
        logger.error(f'Failed to create relation {str(e)[:90]}')
        raise SaveEntityException('Failed to save relation')

def get_all_skills():
    return db.session.query(Skill).all()


def filter_users_by_skill_id(skill_id: int) -> List:
    return db.session.query(User).filter(User.subscriptions.any(id=skill_id)).all()


def filter_users_by_skill_name(skill_dto: SkillsDTO) -> List:
    return db.session.query(User).filter(User.subscriptions.any(skill=skill_dto.skill)).all()


def prepare_users(users) -> List:
    return [UserDTO.from_orm(user).dict() for user in users]


class SaveEntityException(Exception):
    def __init__(self,  message):
        self.message = message
        super().__init__(self.message)


class DeleteEntityException(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)
