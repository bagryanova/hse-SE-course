from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app.schemas import schemas
from app.controllers.routers import get_db
from app.logic.database import Base
from app.main import app
from app.models import models
from app.logic import utils

NOW = '2021-09-26T16:29:06.811823'

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    data_base = TestingSessionLocal()
    try:
        yield data_base
    finally:
        data_base.close()


def clean_db():
    data_base = TestingSessionLocal()
    try:
        data_base.query(schemas.Internship).delete()
        data_base.commit()
    finally:
        data_base.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_internship():
    internship = models.Internship(name="first", description="test 1", updated_at=NOW, application_num=0, is_open=True)
    assert internship.name == "first"
    assert internship.description == "test 1"
    assert internship.application_num == 0
    assert internship.is_open


def test_create_user():
    user = models.User(name="first")
    assert user.name == "first"


def test_create_internship_db():
    clean_db()
    internship = models.Internship(name="first", description="test 1", updated_at=NOW, application_num=0, is_open=True)
    res_internship = utils.create_internship(db=TestingSessionLocal(), internship=internship)
    assert res_internship.id == 1
    assert res_internship.name == "first"
    assert res_internship.description == "test 1"
    assert res_internship.application_num == 0
    assert res_internship.is_open


def test_get_internship_by_name():
    internship = utils.get_internship_by_name(db=TestingSessionLocal(), name="first")
    assert internship.id == 1
    assert internship.name == "first"
    assert internship.description == "test 1"
    assert internship.application_num == 0
    assert internship.is_open
    
    
def test_get_internship_by_id():
    internship = utils.get_internship(db=TestingSessionLocal(), internship_id=1)
    assert internship.id == 1
    assert internship.name == "first"
    assert internship.description == "test 1"
    assert internship.application_num == 0
    assert internship.is_open

