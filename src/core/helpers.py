import re

from core.errors import ValidationError


def validate_email(email: str) -> str:
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    email = email.strip().lower()
    if re.match(email_regex, email) is None:
        raise ValidationError("Invalid email address")
    return email
