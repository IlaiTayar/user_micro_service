from typing import Optional, List

from model.base_model.user import User
from database import database
from model.request_model.user_request import UserRequest

TABLE_NAME = "`user`"


async def create_user(user: User) -> int:
    query = f"""
    INSERT INTO {TABLE_NAME} (first_name, last_name, email, age, address, joining_date)
    VALUES (:first_name, :last_name, :email, :age, :address, :joining_date)
    """

    values = {"first_name": user.first_name,
              "last_name": user.last_name,
              "email": user.email,
              "age": user.age,
              "address": user.address,
              "joining_date": user.joining_date,
              }

    return await database.execute(query, values)


async def register_user(user_id: int) -> str:
    query = f"""
    UPDATE {TABLE_NAME}
    SET is_registered = :is_registered
    WHERE user_id = :user_id
    """

    values = {
        "is_registered": True,
        "user_id": user_id
    }

    await database.execute(query, values)
    return "User registered successfully"


async def update_user(user_id: int, user: UserRequest) -> int:
    query = f"""
    UPDATE {TABLE_NAME}
    SET first_name = :first_name, last_name = :last_name, email = :email, age = :age, address = :address
    WHERE user_id = :user_id
    """

    values = {
        "user_id": user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "age": user.age,
        "address": user.address
    }

    return await database.execute(query, values)


async def get_user_by_id(user_id: int) -> Optional[User]:
    query = f"""
    SELECT * FROM {TABLE_NAME} WHERE user_id = :user_id
    """

    result = await database.fetch_one(query, {"user_id": user_id})

    return User(**dict(result)) if result else None


async def get_user_by_email(email: str) -> List[User]:
    query = f"""
    SELECT * FROM {TABLE_NAME} WHERE email = :email
    """

    result = await database.fetch_all(query, {"email": email})

    return [User(**dict(user)) for user in result]


async def delete_user(user_id: int) -> str:
    query = f"""
    DELETE FROM {TABLE_NAME} WHERE user_id = :user_id
    """

    await database.execute(query, {"user_id": user_id})
    return "User deleted successfully"
