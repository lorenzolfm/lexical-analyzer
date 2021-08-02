from typing import Set, Dict, List
from copy import copy

from .Transition import Transition
from .State import State


class FiniteAutomata:
    def __init__(self,
                 states: Set[State],
                 symbols: Set[str],
                 transitions: Set[Transition],
                 initial_state: State,
                 final_states: Set[State]):
        self._states = states
        self._symbols = symbols
        self._transitions = transitions
        self._initial_state = initial_state
        self._final_states = final_states

    def get_states(self) -> Set[State]:
        return self._states

    def get_symbols(self) -> Set[str]:
        return self._symbols

    def get_initial_state(self) -> State:
        return self._initial_state

    def get_transitions(self) -> Set[Transition]:
        return self._transitions

    def get_final_states(self) -> Set[State]:
        return self._final_states

    def __repr__(self):
        """
        estados | a | b |
        -----------------
            A   | B | A |
            B   | B | B |
        """

        string = ""
        for state in self._states:
            string += f"|{state.get_name()}"
            for symbol in self._symbols:
                for transition in self._transitions:
                    if state == transition.get_origin_state() and symbol == transition.get_symbol():
                        string += f"|{transition.get_destiny_state()}|"
            string += "\n"
        return string

    def determinization(self) -> Dict[State, Set[State]]:
        e_closure: Dict[State, Set[State]] = {state: {state} for state in self._states}

        if ("&" not in self._symbols):
            return e_closure

        for state, values in e_closure.items():
            stack: List[State] = list(copy(values))

            while len(stack):
                actual_state = stack.pop()

                for transition in self._transitions:
                    if actual_state == transition.get_origin_state() and transition.get_symbol() == "&":
                        destiny_state = transition.get_destiny_state()
                        if (destiny_state not in e_closure[state]):
                            e_closure[state].add(destiny_state)
                            stack.append(destiny_state)
        return e_closure
