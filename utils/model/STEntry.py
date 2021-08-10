class STEntry:
    def __init__(self, token: str, lexeme: str, position: int):
        self._token: str = token
        self._lexeme: str = lexeme
        self._position: int = position
