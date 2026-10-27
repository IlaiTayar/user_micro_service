from enum import Enum

from pydantic import BaseModel

from datetime import date


class User(BaseModel):
    user_id: int = None
    first_name: str
    last_name: str
    email: str
    age: int
    address: str
    joining_date: date
    is_registered: bool = False


class UserException(Enum):
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_EXISTS = "USER_EXISTS"