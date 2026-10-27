from datetime import datetime, timezone
from typing import Optional, Union

from model.base_model.user import User, UserException
from model.requst_model.user_request import UserRequest
from repository import user_repository


async def create_user(user: UserRequest) -> Union[str, UserException]:
    existing_user: Optional[User] = await user_repository.get_user_by_email(user.email)
    if existing_user:
        return UserException.USER_EXISTS

    new_user: User = User(**user.model_dump())
    new_user.joining_date = datetime.now(timezone.utc)

    user_id = await user_repository.create_user(new_user)

    return (f"user with mail: {new_user.email} created successfully. "
            f"\nid assigned to user: {user_id}")