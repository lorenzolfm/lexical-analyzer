from State import State


class Transition:
    def __init__(self, origin_state: State, symbol: chr, destiny_state: State):
        self._origin_state = origin_state
        self._symbol = symbol
        self._destiny_state = destiny_state

    def get_origin_state(self) -> State:
        return self._origin_state

    def get_symbol(self) -> chr:
        return self._symbol

    def get_destiny_state(self) -> State:
        return self._destiny_state
