from collections.abc import Callable

type EmailValidatorFunc = Callable[[str], str]
