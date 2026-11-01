from typing import Optional

import httpx
from fastapi import HTTPException

from database import config


async def _get_from_poll_service(url: str, params: Optional[dict] = None) -> dict:
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url, params=params)
    except (httpx.ConnectError, httpx.TimeoutException) as err:
        raise HTTPException(
            status_code=503,
            detail=f"User Service unavailable: {err}"
        )
    except httpx.HTTPError as err:
        raise HTTPException(
            status_code=502,
            detail=f"Error communicating with User Service: {err}"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=response.json().get("detail", "User not found")
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="User Service returned an error"
        )

    return response.json()


async def get_poll_info(poll_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/poll/get/{poll_id}/details"
    return await _get_from_poll_service(url)


async def answer_poll_question() -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/create"
    return await _get_from_poll_service(url)


async def update_answer(answer_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/update/{answer_id}"
    return await _get_from_poll_service(url)


async def delete_answer(answer_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/delete/{answer_id}"
    return await _get_from_poll_service(url)


async def get_user_answers(user_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/get/user/{user_id}"
    return await _get_from_poll_service(url)