from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    age: int
    address: str
    joining_date: date
    is_registered: bool = False


class UserException(Enum):
    USER_NOT_FOUND = "USER NOT FOUND"
    USER_EXISTS = "USER EXISTS"
    MAIL_EXISTS = "MAIL EXISTS FOR ANOTHER USER"