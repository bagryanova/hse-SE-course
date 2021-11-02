from sqlalchemy.orm.session import Session

from app.schemas import schemas
from app.models import models


def create_internship(db: Session, internship: models.Internship):
    db_internship = schemas.Internship(name=internship.name, description=internship.description,
                                       updated_at=internship.updated_at,
                                       is_open=internship.is_open, application_num=internship.application_num)
    db.add(db_internship)
    db.commit()
    db.refresh(db_internship)
    return db_internship


def get_internship_by_name(db: Session, name: str):
    return db.query(schemas.Internship).filter(schemas.Internship.name == name).first()


def get_internship(db: Session, internship_id: int):
    return db.query(schemas.Internship).filter(schemas.Internship.id == internship_id).first()


def create_user(db: Session, user: models.User):
    db_user = schemas.User(name=user.name, sex=user.sex)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

def get_user_by_name(db: Session, name: str):
    return db.query(schemas.User).filter(schemas.User.name == name).first()


def get_users_by_sex(db: Session, user_sex: str):
    return db.query(schemas.User).filter(schemas.User.sex == user_sex)


def get_user(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.id == user_id).first()


def get_internship_by_availability(db: Session, internship_open: bool):
    return db.query(schemas.Internship).filter(schemas.Internship.is_open == internship_open).first()
