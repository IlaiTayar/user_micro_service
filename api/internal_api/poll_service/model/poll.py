from typing import List

from pydantic import BaseModel

from api.internal_api.poll_service.model.question import Question


class Poll(BaseModel):
    poll_id: int
    poll_name: str
    questions: List[Question]
