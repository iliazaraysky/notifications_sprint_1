from pydantic import BaseModel


class Event(BaseModel):
    service: str
    routing_key: str
    body: str
