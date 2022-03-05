import hashlib

from exceptions import CustomException


def generate_sign(sign_bytes_string: bytes) -> str:
    """Generates sign for payments"""

    try:
        return hashlib.sha256(sign_bytes_string).hexdigest()
    except TypeError as exc:
        raise CustomException(
            f"Invalid sign string provided: {sign_bytes_string}, exception")
