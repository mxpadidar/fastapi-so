from collections.abc import Callable

from account.service_layer.dtos import TokenDto

type PasswordHashingFunc = Callable[[str], str]

type PasswordVerifierFunc = Callable[[str, str], bool]

type TokenParserFunc = Callable[[str], int]

type TokenGeneratorFunc = Callable[[int], TokenDto]
