from typing import Optional

from .Token import Token


class State:
    def __init__(self, name: str, label: str = "", token: Optional[Token] = None) -> None:
        self._name = name
        self._label = label
        self._token = token

    def get_name(self) -> str:
        return self._name

    def get_label(self) -> str:
        return self._label

    def get_token(self) -> Optional[Token]:
        return self._token

    def set_token(self, token: Token) -> None:
        self._token = token
        return None

    def __repr__(self) -> str:
        return self.get_name()
