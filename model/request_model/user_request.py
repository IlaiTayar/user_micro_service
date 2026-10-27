from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    first_name: str = Field(..., min_length=2)
    last_name: str = Field(..., min_length=2)
    email: str = Field(..., min_length=8)
    age: int = Field(..., gt=0)
    address: str = Field(..., min_length=1)