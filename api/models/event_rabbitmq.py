from pydantic import BaseModel


class Event(BaseModel):
    queue_name: str
    body: str