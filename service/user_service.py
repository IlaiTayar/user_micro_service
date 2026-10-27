from datetime import datetime, timezone
from typing import Optional, Union

from model.base_model.user import User, UserException
from model.request_model.user_request import UserRequest
from repository import user_repository


async def create_user(user: UserRequest) -> Union[str, UserException]:
    existing_user: Optional[User] = await user_repository.get_user_by_email(user.email)
    if existing_user:
        return UserException.USER_EXISTS

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        age=user.age,
        address=user.address,
        joining_date=datetime.now(timezone.utc).date(),
        is_registered=False
    )

    user_id = await user_repository.create_user(new_user)

    return (f"user with mail: {new_user.email} created successfully. "
            f"\nid assigned to user: {user_id}")