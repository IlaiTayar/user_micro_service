from typing import Optional

from pydantic import BaseModel

from api.internal_api.poll_service.model.option import Option
from api.internal_api.poll_service.model.question import Question


class UserAnswer(BaseModel):
    user_id: int
    question_answer: dict[Question, Optional[Option]]