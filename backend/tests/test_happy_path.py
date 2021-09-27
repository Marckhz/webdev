import unittest
from typing import Dict, List

from app import app, create_users
from models import db

from .fixtures import get_user_data, get_user_skill_data


class HappyPathApiTest(unittest.TestCase):
    TESTING = True

    def setUp(self) -> None:
        with app.app_context():
            create_users()
    
    def tearDown(self) -> None:
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_add_user(self):
        data = get_user_data()
        with app.test_client() as c:
            rv = c.post("/api/users",json=data)
        assert rv.status_code == 201
        assert 'msg' in rv.json.keys()
    
    def test_fetch_all_users(self):
        with app.test_client() as c:
            rv = c.get('/api/users')
        assert rv.status_code == 200
        self.assertIsInstance(rv.json, List)
    
    def test_fetch_user_by_id(self):
        with app.test_client() as c:
            rv = c.get('api/users/1')
        assert rv.status_code == 200
        self.assertIsInstance(rv.json, Dict)
    
    def test_create_skill(self):
        data = get_user_skill_data()
        with app.test_client() as c:
            rv = c.post('api/users/create-skill', json=data)
        assert rv.status_code == 201
        self.assertIsInstance(rv.json, Dict)
    
    def test_fetch_skills(self):
        with app.test_client() as c:
            rv = c.get('api/skills')
        assert rv.status_code == 200
        self.assertIsInstance(rv.json, List)
    
    def test_fetch_users_skills(self):
        skill = 'python'
        with app.test_client() as c:
            rv = c.get(f'api/users/skills/{skill}')
        assert rv.status_code == 200
        self.assertIsInstance(rv.json, List)

    def test_add_user_wrong_data(self):
        with app.test_client() as c:
            rv = c.post('api/users')
        assert rv.status_code == 400
        assert 'msg' in rv.json.keys()
        msg = rv.json.get('msg')
        self.assertEqual(msg , "Input data is incorrect")

    def test_add_wrong_skill(self):
        with app.test_client() as c:
            rv = c.post('api/users/create-skill')
        assert rv.status_code == 400
        assert "msg" in rv.json.keys()
        msg = rv.json.get('msg')
        self.assertEqual(msg,"data input incorrect")