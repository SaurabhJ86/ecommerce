from dataclasses import dataclass
from enum import Enum, auto

class UserType(Enum):
    PRIME = auto()
    NORMAL = auto()
    PRIVILEGED = auto()
    UBER = auto()


@dataclass
class User:
    name: str
    email: str
    phone: str
    status: bool
    user_type: UserType
