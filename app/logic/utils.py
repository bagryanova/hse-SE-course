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
