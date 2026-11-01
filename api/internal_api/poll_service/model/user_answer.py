from typing import Optional

from pydantic import BaseModel

from api.internal_api.poll_service.model.option import Option


class UserAnswer(BaseModel):
    user_id: int
    question_answer: dict[int, Optional[Option]]