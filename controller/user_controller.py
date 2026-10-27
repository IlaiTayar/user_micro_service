from typing import Union

from fastapi import APIRouter, HTTPException
from starlette import status

from model.base_model.user import UserException
from model.requst_model.user_request import UserRequest
from service import user_service

router: APIRouter = APIRouter(prefix="/user",
                              tags=["user"])


def _exception_handler(result: Union[str, UserException]) -> None:
    if result == UserException.USER_NOT_FOUND:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{result.name}")

    if result == UserException.USER_EXISTS:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{result.name}")




@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest) -> str:
    result: Union[str, UserException] = await user_service.create_user(user)
    _exception_handler(result)
    return f"{result}"
