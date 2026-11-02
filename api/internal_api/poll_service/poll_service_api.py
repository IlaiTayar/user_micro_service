import httpx
from fastapi import HTTPException

from database import config


async def get_poll_info(poll_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/poll/get/{poll_id}/details"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            try:
                detail = exc.response.json().get("detail", "Resource not found")
            except ValueError:
                detail = exc.response.text or "Resource not found"
            raise HTTPException(status_code=404, detail=detail) from exc

        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error",
        ) from exc
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise HTTPException(
            status_code=503,
            detail="Poll Service is unavailable",
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with Poll Service",
        ) from exc

    return response.json()


async def answer_poll_question(answer) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/create"

    if isinstance(answer, dict):
        payload = answer
    else:
        payload = {
            "user_id": answer.user_id,
            "question_id": answer.question_id,
            "option_id": answer.option_id,
        }

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            try:
                detail = exc.response.json().get("detail", "Resource not found")
            except ValueError:
                detail = exc.response.text or "Resource not found"
            raise HTTPException(status_code=404, detail=detail) from exc

        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error",
        ) from exc
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise HTTPException(
            status_code=503,
            detail="Poll Service is unavailable",
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with Poll Service",
        ) from exc

    return response.json()


async def update_answer(answer_id: int, answer) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/update/{answer_id}"

    if isinstance(answer, dict):
        payload = answer
    else:
        payload = {
            "user_id": answer.user_id,
            "question_id": answer.question_id,
            "option_id": answer.option_id,
        }

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.put(url, json=payload)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            try:
                detail = exc.response.json().get("detail", "Resource not found")
            except ValueError:
                detail = exc.response.text or "Resource not found"
            raise HTTPException(status_code=404, detail=detail) from exc

        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error",
        ) from exc
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise HTTPException(
            status_code=503,
            detail="Poll Service is unavailable",
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with Poll Service",
        ) from exc

    return response.json()


async def delete_answer(answer_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/delete/{answer_id}"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.delete(url)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            try:
                detail = exc.response.json().get("detail", "Resource not found")
            except ValueError:
                detail = exc.response.text or "Resource not found"
            raise HTTPException(status_code=404, detail=detail) from exc

        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error",
        ) from exc
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise HTTPException(
            status_code=503,
            detail="Poll Service is unavailable",
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with Poll Service",
        ) from exc

    return response.json()


async def get_user_answers(user_id: int) -> dict:
    url = f"{config.POLL_SERVICE_URL}/user_answer/get/by-user/{user_id}"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            try:
                detail = exc.response.json().get("detail", "Resource not found")
            except ValueError:
                detail = exc.response.text or "Resource not found"
            raise HTTPException(status_code=404, detail=detail) from exc

        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error",
        ) from exc
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise HTTPException(
            status_code=503,
            detail="Poll Service is unavailable",
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with Poll Service",
        ) from exc

    return response.json()


async def delete_answers_by_user(user_id: int) -> str:
    url = f"{config.POLL_SERVICE_URL}/user_answer/delete/user/{user_id}"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.delete(url)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            try:
                detail = exc.response.json().get("detail", "Resource not found")
            except ValueError:
                detail = exc.response.text or "Resource not found"
            raise HTTPException(status_code=404, detail=detail) from exc

        raise HTTPException(
            status_code=502,
            detail="Poll Service returned an error",
        ) from exc
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise HTTPException(
            status_code=503,
            detail="Poll Service is unavailable",
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with Poll Service",
        ) from exc

    return response.json()
