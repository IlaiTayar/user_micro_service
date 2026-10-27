from typing import Optional

from model.base_model.user import User
from database import database


TABLE_NAME = "`user`"


async def create_user(user: User) -> int:
    query = f"""
    INSERT INTO {TABLE_NAME} (first_name, last_name, age, address, email, joining_date)
    VALUES (:first_name, :last_name, :age, :address, :email, :joining_date)
    """

    values = {"first_name": user.first_name,
              "last_name": user.last_name,
              "age": user.age,
              "address": user.address,
              "email": user.email,
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


async def update_user(user_id: int, user: User) -> int:
    query = f"""
    UPDATE {TABLE_NAME}
    SET first_name = :first_name, last_name = :last_name, age = :age, address = :address, email = :email, is_registered = :is_registered
    WHERE user_id = :user_id
    """

    values = {
        "user_id": user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "address": user.address,
        "email": user.email,
        "is_registered": user.is_registered
    }

    return await database.execute(query, values)


async def get_user(user_id: int) -> Optional[User]:
    query = f"""
    SELECT * FROM {TABLE_NAME} WHERE user_id = :user_id
    """

    result = await database.fetch_one(query, {"user_id": user_id})

    return User(**dict(result)) if result else None


async def get_user_by_email(email: str) -> Optional[User]:
    query = f"""
    SELECT * FROM {TABLE_NAME} WHERE email = :email
    """

    result = await database.fetch_one(query, {"email": email})

    return User(**dict(result)) if result else None


async def delete_user(user_id: int) -> str:
    query = f"""
    DELETE FROM {TABLE_NAME} WHERE user_id = :user_id
    """

    await database.execute(query, {"user_id": user_id})
    return "User deleted successfully"
