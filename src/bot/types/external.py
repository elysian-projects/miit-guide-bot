from enum import Enum, unique
from typing import Any

from aiogram import types as AIOGramTypes


class Enumerable(Enum):
    def __getitem__(self, name) -> Any:
        return format(self[name])

    def __str__(self) -> str:
        return format(self.value)
