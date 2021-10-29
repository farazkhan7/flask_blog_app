import pytest
from flaskblog.config import TestConfig
import os
from flaskblog import create_app, db


# session scope fixture seems to outlive a test execution using package scope instead
@pytest.fixture(scope='package', autouse=True)
def client():
    app = create_app(TestConfig)
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context() as c:
            db.init_app(app)
            db.create_all()

            yield client
        # tear down
    with app.app_context():
        db.session.remove()
        db.drop_all()
        os.remove('flaskblog/test.db')

    # os.close(db)
    # os.unlink(config.db_path)
    # os.unlink('sqlite:///test.db')