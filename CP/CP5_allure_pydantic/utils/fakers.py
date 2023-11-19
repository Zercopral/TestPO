from random import choice, randint
from string import ascii_letters, digits
from datetime import datetime


def random_number(start: int = 100, end: int = 1000) -> int:
    return randint(start, end)


def random_string(start: int = 9, end: int = 15) -> str:
    return "".join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_boolean() -> bool:
    return bool(randint(0, 1))


def random_date() -> str:
    return datetime.now().isoformat(sep="T")
