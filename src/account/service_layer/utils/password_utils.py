import bcrypt

from account.service_layer import types


def password_hashing_func_closure(salt: str) -> types.PasswordHashingFunc:
    """
    Closure to create a password hashing function with a salt.
    """

    def hash_password_with_salt(password: str) -> str:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt.encode("utf-8"))
        return hashed_password.decode("utf-8")

    return hash_password_with_salt


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify the password against the password hash.
    """

    return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))
