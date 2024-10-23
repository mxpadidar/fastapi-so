import pytest

from core.errors import ValidationError
from core.helpers import validate_email


def test_validate_email_valid():
    assert validate_email("test@example.com") == "test@example.com"
    assert validate_email("TEST@EXAMPLE.COM") == "test@example.com"
    assert validate_email("test.email+alias@example.com") == "test.email+alias@example.com"
    assert validate_email("  test@example.com  ") == "test@example.com"
    assert validate_email("\ttest@example.com\t") == "test@example.com"
    assert validate_email("\ntest@example.com\n") == "test@example.com"


def test_validate_email_invalid():
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("invalid-email")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("invalid-email@")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("invalid-email@example")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("invalid-email@example.")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("invalid-email@example.c")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("invalid-email@.com")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("@example.com")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("test@.com")
    with pytest.raises(ValidationError, match="Invalid email address"):
        validate_email("test@com")
