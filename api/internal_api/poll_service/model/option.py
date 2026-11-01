from pydantic import BaseModel


class Option(BaseModel):
    option_id: int
    question_id: int
    option_text: str