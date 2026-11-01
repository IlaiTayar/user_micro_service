from typing import List

from pydantic import BaseModel

from api.internal_api.poll_service.model.option import Option


class Question(BaseModel):
    question_id: int
    question_text: str
    options: List[Option]