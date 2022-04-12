import hashlib
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

from exceptions import InvalidTypeProvided, InvalidCurrencyValue


def generate_sign(sign_bytes_string: bytes) -> str:
    """Generates sign for payments"""

    try:
        return hashlib.sha256(sign_bytes_string).hexdigest()
    except TypeError as exc:
        raise InvalidTypeProvided(
            f"Invalid sign byte string provided: {sign_bytes_string}, exception: {exc}")


def get_utc_now():
    """Gets current datetime in UTC"""

    return datetime.now(timezone.utc)


def validate_value(value: str) -> Decimal:
    """Validates currency value"""

    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise InvalidCurrencyValue(
            f"Provided invalid currency value: {value}, exception: {exc}")
