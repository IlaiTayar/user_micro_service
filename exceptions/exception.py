from fastapi import HTTPException
from starlette import status


def user_not_found_exception(user_id: int) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} was not found"
    )


def mail_exists_exception(email: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"User with email '{email}' already exists"
    )


def user_is_registered_exception(user_id: int) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"User with id {user_id} is already registered"
    )


def missing_fields_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="Missing required fields"
    )
