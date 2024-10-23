from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

import bcrypt
import jwt

from core.errors import UnAuthenticatedError


@dataclass
class Token:
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

    def to_dict(self) -> dict:
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "token_type": self.token_type,
        }


class AuthService:
    """
    Service for handling authentication and authorization.
    """

    def __init__(self, pass_salt: str, secret: str, algorithm: str, access_exp_min: int, refresh_exp_day: int) -> None:
        """
        Initialize the AuthService with the given parameters.

        Args:
            pass_salt (str): The salt used for hashing passwords.
            secret (str): The secret key used for encoding and decoding JWT tokens.
            algorithm (str): The algorithm used for encoding and decoding JWT tokens.
            access_exp_min (int): The expiration time in minutes for access tokens.
            refresh_exp_day (int): The expiration time in days for refresh tokens.
        """

        self.pass_salt: str = pass_salt
        self.secret: str = secret
        self.algorithm: str = algorithm
        self._access_exp_min: int = access_exp_min
        self._refresh_exp_day: int = refresh_exp_day

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verify the plain password against the hashed password.

        Args:
            plain_password (str): The plain text password to verify.
            hashed_password (str): The hashed password to verify against.

        Returns:
            bool: True if the password matches, False otherwise.
        """

        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    def get_password_hash(self, password: str) -> str:
        """
        Generate a hashed password.

        Args:
            password (str): The plain text password to hash.

        Returns:
            str: The hashed password.
        """

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), self.pass_salt.encode("utf-8"))
        return hashed_password.decode("utf-8")

    def generate_tokens(self, user_id: int) -> Token:
        """
        Generate access and refresh tokens.

        Args:
            user_id (int): The user ID for which to generate tokens.

        Returns:
            Token: The generated access and refresh tokens.
        """

        access_token = self._generate_access_token(user_id)
        refresh_token = self._generate_refresh_token(user_id)
        return Token(access_token=access_token, refresh_token=refresh_token)

    def decode_token(self, token: str) -> int:
        """
        Decode the token.

        Args:
            token (str): The JWT token to decode.

        Returns:
            int: The user ID if the token is valid.

        Raises:
            UnAuthenticatedError: If the token is invalid.
        """

        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return payload["sub"]
        except (
            jwt.ExpiredSignatureError,
            jwt.InvalidSignatureError,
            jwt.InvalidTokenError,
        ):
            raise UnAuthenticatedError("Invalid token.")

    def get_bearer_token(self, auth_header: str | None) -> str:
        """
        Extract the bearer token from the authorization header.

        Args:
            auth_header (str | None): The authorization header containing the bearer token.

        Returns:
            str: The extracted bearer token.

        Raises:
            UnAuthenticatedError: If the token is missing or invalid.
        """

        if not auth_header:
            raise UnAuthenticatedError("Missing authorization header.")

        parts = auth_header.split()

        if len(parts) != 2 or parts[0].lower() != "bearer":
            raise UnAuthenticatedError("Invalid authorization header format.")

        return parts[1]

    def _generate_access_token(self, sub) -> str:
        expires_at = datetime.now(tz=UTC) + timedelta(minutes=self._access_exp_min)
        payload = {"sub": sub, "type": "access", "exp": expires_at.timestamp()}
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def _generate_refresh_token(self, sub) -> str:
        expires_in = datetime.now(tz=UTC) + timedelta(days=self._refresh_exp_day)
        payload = {"sub": sub, "type": "refresh", "exp": expires_in.timestamp()}
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)
