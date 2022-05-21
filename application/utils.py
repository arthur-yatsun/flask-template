from datetime import datetime, timezone

from exceptions import FieldNotFound


def get_utc_now():
    """Function to get the current datetime in UTC"""
    return datetime.now(timezone.utc)


def get_app_config_variable(current_app: "Flask", name: str):
    """Function to get the variable from the app config"""

    try:
        return current_app.config[name]
    except KeyError:
        raise FieldNotFound(f"{name} variable wasn't found in the provided app config")
