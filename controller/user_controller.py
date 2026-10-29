from fastapi import APIRouter, HTTPException
from starlette import status

from model.base_model.user import User
from model.request_model.user_request import UserRequest
from service import user_service

router: APIRouter = APIRouter(prefix="/user",
                              tags=["user"])


def _exception_handler(result):
    if isinstance(result, HTTPException):
        raise result
    return result


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest) -> str:
    result = await user_service.create_user(user)
    return _exception_handler(result)


@router.put("/register/{user_id}", status_code=status.HTTP_200_OK)
async def register_user(user_id: int) -> str:
    result = await user_service.register_user(user_id)
    return _exception_handler(result)


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UserRequest) -> str:
    result = await user_service.update_user(user_id, user)
    return _exception_handler(result)


@router.get("/get/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int) -> User:
    result = await user_service.get_user_by_id(user_id)
    return _exception_handler(result)
