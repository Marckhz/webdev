import logging

from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from dto.requests_payload import SkillsDTO, UserDTO, UserSkillDTO
from models.repository import (SaveEntityException, delete_users,
                               filter_users_by_skill_name, get_all_skills,
                               get_all_users, get_user_by_id, prepare_users,
                               save_user, save_user_skill)

logger = logging.getLogger(__name__)
general = Blueprint('general', __name__)


@general.route('/users', methods=['POST'])
def create_users():
    data = request.get_json()
    try:
        user_dto = UserDTO(**data)
        save_user(user_dto)
        return jsonify({"msg": "Created"}), 201
    except (SaveEntityException, TypeError, ValidationError) as e:
        logger.error(f'While creating user got the next error: {e}')
        return jsonify({'msg': 'Input data is incorrect'}), 400


@general.route("/users", methods=["DELETE"])
def delete_all_users():
    delete_users()
    return jsonify({"msg": "Users Deleted"}), 200


@general.route("/users", methods=["GET"])
def users():
    result = get_all_users()
    users = []
    if result:
        users = prepare_users(result)
    return jsonify(users if users else []), 200


@general.route('/users/<user_id>', methods=['GET'])
def user_data(user_id):
    result = get_user_by_id(user_id)
    if result:
        UserDTO.update_forward_refs()
        user = UserDTO.from_orm(result)
    return jsonify(user.dict() if user else {}), 200


@general.route("/users/skills/<skill>", methods=['GET'])
def select_users_skill(skill):
    users = []
    skill_dto = SkillsDTO(skill=skill)
    result = filter_users_by_skill_name(skill_dto)
    if result:
        users = prepare_users(result)
    return jsonify(users if users else []), 200


@general.route('/users/create-skill', methods=['POST'])
def create_skills():
    data = request.get_json()
    try:
        dto = UserSkillDTO(**data)
        save_user_skill(dto)
    except (SaveEntityException, TypeError, ValidationError) as e:
        logger.error(f'while saving skills got the following error {e}')
        return jsonify({"msg": 'data input incorrect'}), 400
    return jsonify(dto.dict()), 201


@general.route('/skills', methods=['GET'])
def skills():
    result = get_all_skills()
    skills = []
    if result:
        for s in result:
            skills_obj = SkillsDTO.from_orm(s).dict()
            skills.append(skills_obj)
    return jsonify(skills if skills else []), 200
