now = '2021-09-26T16:29:06.811823'


def test_create_internship():
    internship = models.Internship(name="first", description="test 1", updated_at=now, application_num=0, is_open=True)
    assert internship.id == 1
    assert internship.name == "first"
    assert internship.description == "test 1"
    assert internship.application_num == 0
    assert internship.is_open
