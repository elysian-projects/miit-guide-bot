from enum import Enum, unique
from typing import Any

from aiogram import types as AIOGramTypes


class Enumerable(Enum):
    def __get__(self, _, __) -> Any:
        return format(self.value)

    def __getitem__(self) -> str:
        return format(self.value)

    def __str__(self) -> str:
        return format(self.value)
