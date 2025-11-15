from _datetime import datetime

from pydantic import BaseModel


class AnonymousBoardResponse(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime
    # created_at: str
