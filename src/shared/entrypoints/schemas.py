from pydantic import BaseModel
from pydantic_core import Url


class FileResponse(BaseModel):
    id: int
    name: str
    size: int
    url: Url
