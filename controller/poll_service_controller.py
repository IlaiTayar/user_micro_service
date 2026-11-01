from fastapi import APIRouter, HTTPException
from starlette import status

from api.internal_api.poll_service import poll_service_api
from api.internal_api.poll_service.model.answer import Answer

router: APIRouter = APIRouter(prefix="/poll", tags=["poll"])


@router.post("/answer", status_code=status.HTTP_201_CREATED)
async def create_answer(answer: Answer):
    return await poll_service_api.answer_poll_question(answer=answer)


@router.put("/update", status_code=status.HTTP_200_OK)
async def update_answer(answer_id: int, answer: Answer):
    return await poll_service_api.update_answer(answer_id=answer_id, answer=answer)


@router.get("/get/poll/{poll_id}/details", status_code=status.HTTP_200_OK)
async def get_poll_details(poll_id: int):
    return await poll_service_api.get_poll_info(poll_id=poll_id)

@router.delete("/delete/answer/{answer_id}", status_code=status.HTTP_200_OK)
async def delete_answer_by_id(answer_id: int):
    return await poll_service_api.delete_answer(answer_id=answer_id)