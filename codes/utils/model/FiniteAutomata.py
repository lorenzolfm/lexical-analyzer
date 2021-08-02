from typing import Set, Dict, List, Optional
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

    def determinization(self) -> None:
        if ("&" not in self._symbols):
            return None

        e_closure = self._get_e_closure()
        new_initial_state = e_closure[self._initial_state]
        new_states: Set[Set[State]] = set(e_closure.values())
        new_final_states = self._get_new_final_states(new_states)
        self._symbols.remove("&")

        return None

    def _get_new_transitions(self, list_of_new_states: Set[Set[State]]) -> Set[Transition]:
        new_transitions: Set[Transition] = set()

        return self._transitions

    def _get_new_final_states(self, list_of_new_states: Set[Set[State]]) -> Set[Set[State]]:
        new_final_states: Set[Set[State]] = set()
        for new_states in list_of_new_states:
            for state in new_states:
                if state in self._final_states:
                    new_final_states.add(new_states)

        return new_final_states

    def _get_e_closure(self) -> Dict[State, Set[State]]:
        e_closure: Dict[State, Set[State]] = {state: {state} for state in self._states}

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

    def _get_transition(self, origin, symbol) -> Optional[Transition]:
        for transition in self._transitions:
            if origin == transition.get_origin_state() and symbol == transition.get_symbol():
                return transition

        return None
