from typing import List

from Transition import Transition
from State import State


class FiniteAutomata:
    def __init__(self,
                 states: List[State],
                 symbols: List[chr],
                 transitions: List[Transition],
                 initial_state: State,
                 final_states: List[State]):
        self._states = states
        self._symbols = symbols
        self._transitions = transitions
        self._initial_state = initial_state
        self._final_states = final_states

    def get_states(self) -> List[State]:
        return self._states

    def get_symbols(self) -> List[chr]:
        return self._symbols

    def get_initial_state(self) -> State:
        return self._initial_state

    def get_transitions(self) -> List[Transition]:
        return self._transitions

    def get_final_states(self) -> List[State]:
        return self._final_states
