from .State import State


class Transition:
    def __init__(self, origin_state: State, symbol: str, destiny_state: State) -> None:
        self._origin_state = origin_state
        self._symbol = symbol
        self._destiny_state = destiny_state

    def get_origin_state(self) -> State:
        return self._origin_state

    def get_symbol(self) -> str:
        return self._symbol

    def get_destiny_state(self) -> State:
        return self._destiny_state

    def __repr__(self) -> str:
        return f"{self._origin_state, self._symbol, self._destiny_state}"
