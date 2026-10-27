from typing import Union, Optional

from fastapi import APIRouter, HTTPException, Query
from starlette import status

from model.base_model.user import UserException, User
from model.request_model.user_request import UserRequest
from service import user_service

router: APIRouter = APIRouter(prefix="/user",
                              tags=["user"])


def _exception_handler(result):
    if isinstance(result, UserException):
        if result == UserException.USER_NOT_FOUND:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{result.value}")

        if result == UserException.USER_EXISTS:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{result.value}")

        if result == UserException.MAIL_EXISTS:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{result.value}")

        if result == UserException.USER_IS_REGISTERED:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{result.value}")

        if result == UserException.MISSING_FIELDS:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=f"{result.value}")

    return result


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest) -> str:
    result: Union[str, UserException] = await user_service.create_user(user)

    _exception_handler(result)
    return f"{result}"


@router.put("/register/id-{user_id}", status_code=status.HTTP_200_OK)
async def register_user(user_id: int) -> str:
    result = await user_service.register_user(user_id)

    _exception_handler(result)
    return f"{result}"


@router.put("/update/id-{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UserRequest) -> str:
    result: Union[str, UserException] = await user_service.update_user(user_id, user)

    _exception_handler(result)
    return f"{result}"


@router.get("/search", response_model=User, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: Optional[int] = Query(None)) -> User:
    result: Union[User, UserException] = await user_service.get_user_by_id(user_id)

    result = _exception_handler(result)
    return result