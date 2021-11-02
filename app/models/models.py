import datetime
from typing import Optional

from pydantic.main import BaseModel


class Internship(BaseModel):
    name: str
    description: Optional[str] = None
    updated_at: datetime.datetime
    application_num: Optional[int] = None
    is_open: bool


class User(BaseModel):
    name: str
    sex: str
