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
            detail=f"Poll Service is unavailable: {err}"
        )
    except httpx.HTTPError as err:
        raise HTTPException(
            status_code=502,
            detail=f"Error communicating with Poll Service: {err}"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=response.json().get("detail", "Resource not found")
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error"
        )

    return response.json()


async def _request_to_poll_service(method: str, url: str, json_body: Optional[dict] = None, params: Optional[dict] = None) -> dict:
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.request(method, url, json=json_body, params=params)
    except (httpx.ConnectError, httpx.TimeoutException) as err:
        raise HTTPException(
            status_code=503,
            detail=f"Poll Service is unavailable: {err}"
        )
    except httpx.HTTPError as err:
        raise HTTPException(
            status_code=502,
            detail=f"Error communicating with Poll Service: {err}"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=response.json().get("detail", "Resource not found")
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error"
        )

    return response.json()


async def get_poll_info(poll_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/poll/get/{poll_id}"
    return await _get_from_poll_service(url)


async def answer_poll_question(payload: dict) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/create"
    return await _request_to_poll_service("POST", url, json_body=payload)


async def update_answer(answer_id: int, payload: dict) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/update/{answer_id}"
    return await _request_to_poll_service("PUT", url, json_body=payload)


async def delete_answer(answer_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/delete/{answer_id}"
    return await _request_to_poll_service("DELETE", url)


async def get_user_answers(user_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/get/user/{user_id}"
    return await _get_from_poll_service(url)
