from sqlalchemy.sql.functions import now
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime

from app.logic.database import Base


class Internship(Base):
    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    updated_at = Column(DateTime(timezone=True), default=now())
    application_num = Column(Integer, default=0)
    is_open = Column(Boolean, default=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(String)
    status = Column(String)
