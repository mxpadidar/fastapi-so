import os
from uuid import uuid4

from magic import Magic

from core.errors import ValidationError


def get_file_mime_type(file_content: bytes) -> str:
    """Determine the MIME type of the given file content."""
    mime = Magic(mime=True)
    mime_type = mime.from_buffer(file_content)
    return mime_type


def generate_unique_filename(filename: str) -> str:
    """Generate a unique filename for the given file."""
    try:
        _, extension = os.path.splitext(filename)
    except ValueError:
        raise ValidationError("Invalid file name")
    return f"{uuid4()}{extension}"
