from dataclasses import dataclass

from core.base_classes.base_dto import BaseDto


@dataclass
class TokenDto(BaseDto["TokenDto"]):
    access_token: str
    refresh_token: str
    token_type: str
