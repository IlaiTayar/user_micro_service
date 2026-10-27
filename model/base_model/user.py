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
    MAIL_EXISTS = "MAIL EXISTS FOR ANOTHER USER"
    USER_IS_REGISTERED = "USER IS REGISTERED"
    MISSING_FIELDS = "MISSING FIELDS"