import logging

import coloredlogs
from faker import Faker
from flask import Flask, current_app
from flask_cors import CORS
from flask_migrate import Migrate

from blueprints.general import general
from config import get_config
from fixtures.fixtures import init
from models import db

#if create app, then we need to access with context

app = Flask(__name__)
app.config.from_object(get_config())
cors = CORS(app)
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
db.init_app(app)
migrate = Migrate(app, db)


# TODO 
# populate  on first request
@app.before_first_request
def create_users():
    if app.config['DATABASE_DROP_CREATE_ALL']:
        logger.info('App database\'s tables will be recreated')
        db.drop_all()
        db.create_all()
    if app.config['POPULATE_WITH_FIXTURES']:
        logger.info(f'App database\'s tables will be populated with fake data')
        init(db, current_app.config)

app.register_blueprint(general, url_prefix=f'{app.config["APPLICATION_ROOT"]}/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

