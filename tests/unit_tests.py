from app.models import models

now = '2021-09-26T16:29:06.811823'


def test_create_internship():
    internship = models.Internship(name="first", description="test 1", updated_at=now, application_num=0, is_open=True)
    assert internship.name == "first"
    assert internship.description == "test 1"
    assert internship.application_num == 0
    assert internship.is_open


def test_create_user():
    user = models.User(name="first")
    assert user.name == "first"

