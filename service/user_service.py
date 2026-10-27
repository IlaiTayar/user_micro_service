from datetime import datetime, timezone
from typing import Optional, Union, List

from model.base_model.user import User, UserException
from model.request_model.user_request import UserRequest
from repository import user_repository


async def create_user(user: UserRequest) -> Union[str, UserException]:
    existing_user: Optional[List[User]] = await get_user_by_email(user.email)
    if existing_user:
        return UserException.MAIL_EXISTS

    new_user: User = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        age=user.age,
        address=user.address,
        joining_date=datetime.now(timezone.utc).date(),
        is_registered=False
    )

    user_id: int = await user_repository.create_user(new_user)

    return f"user with mail: {new_user.email} created successfully. id assigned to user: {user_id}."


async def register_user(user_id) -> Union[str, UserException]:
    existing_user: Union[User, UserException] = await get_user_by_id(user_id)
    if isinstance(existing_user, UserException):
        return existing_user

    if existing_user and existing_user.is_registered == True:
        return UserException.USER_IS_REGISTERED

    else:
        register: str = await user_repository.register_user(user_id)
        return register


async def update_user(user_id: int, user: UserRequest) -> Union[str, UserException]:
    existing_user: Union[User, UserException] = await get_user_by_id(user_id)
    if isinstance(existing_user, UserException):
        return existing_user

    existing_user_mails: Optional[List[User]] = await get_user_by_email(user.email)
    if existing_user_mails:
        for exist in existing_user_mails:
            if exist.user_id != user_id and exist.email == user.email:
                return UserException.MAIL_EXISTS

    await user_repository.update_user(user_id, user)
    return f"user with mail: {user.email} and id: {user_id} updated successfully."


async def get_user_by_id(user_id: int) -> Union[User, UserException]:
    user: Optional[User] = await user_repository.get_user_by_id(user_id)
    if user is None:
        return UserException.USER_NOT_FOUND

    return user


async def get_user_by_email(user_email: str) -> Optional[List[User]]:
    users: List[User] = await user_repository.get_user_by_email(user_email)
    if len(users) == 0:
        return None

    return users