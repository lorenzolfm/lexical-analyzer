from .Token import Token


class Lexeme:
    def __init__(self, name: str, token: Token) -> None:
        self._name = name
        self._token = token

    def get_name(self) -> str:
        return self._name

    def get_token(self) -> Token:
        return self._token
