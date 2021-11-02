from app.models import models

NOW = '2021-09-26T16:29:06.811823'


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
    internship = models.Internship(name="first", description="test 1", updated_at=NOW, application_num=0, is_open=True)
    res_internship = utils.create_internship(db=TestingSessionLocal(), internship=internship)
    assert res_internship.id == 1
    assert res_internship.name == "first"
    assert res_internship.description == "test 1"
    assert res_internship.application_num == 0
    assert res_internship.is_open
