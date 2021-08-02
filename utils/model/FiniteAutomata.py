from typing import List, Dict
from copy import copy

from .Transition import Transition
from .State import State

class FiniteAutomata:
    def __init__(self,
                 states: List[State],
                 symbols: List[str],
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

    def get_symbols(self) -> List[str]:
        return self._symbols

    def get_initial_state(self) -> State:
        return self._initial_state

    def get_transitions(self) -> List[Transition]:
        return self._transitions

    def get_final_states(self) -> List[State]:
        return self._final_states

    def determinization(self) -> None:
        if not self._symbols.count("&"):
            return None

        e_closure: Dict[State, List[State]] = {state: [state] for state in self._states}

        for state, values in e_closure.items():
            stack: List[State] = copy(values)

            while len(stack):
                actual_state = stack.pop()

                for transition in self._transitions:
                    if actual_state == transition.get_origin_state() and transition.get_symbol() == "&":
                        destiny_state = transition.get_destiny_state()
                        if not e_closure[state].count(destiny_state):
                            e_closure[state].append(destiny_state)
                            stack.append(destiny_state)

        print(e_closure)





