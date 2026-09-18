from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None


class TaskUpdate(BaseModel):
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    model_config = {
        "from_attributes": True
    }