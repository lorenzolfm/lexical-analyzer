from typing import Set, Dict, List, Optional, Tuple
from copy import copy

from .Transition import Transition
from .State import State


class FiniteAutomata:
    def __init__(self,
                 states: Set[State],
                 symbols: Set[str],
                 transitions: Set[Transition],
                 initial_state: State,
                 final_states: Set[State]
                 ) -> None:
        self._states: Set[State] = states
        self._symbols: Set[str] = symbols
        self._transitions: Set[Transition] = transitions
        self._initial_state: State = initial_state
        self._final_states: Set[State] = final_states

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

    def eval_lexeme(self, lexeme: str) -> bool:
        actual_state = self._initial_state
        for char in lexeme:
            transition = self._get_transition(actual_state, char)
            actual_state = transition.get_destiny_state()

        if actual_state in self._final_states:
            return True

        return False

    def _set_new_states(self, list_of_new_transitions: List[Tuple]) -> None:
        self._states = set()
        self._transitions = set()
        new_final_states: Set[State] = set()
        states_names: List[Set[State]] = []
        for transition in list_of_new_transitions:
            origin_state_name: set = transition[0]
            destiny_state_name: set = transition[2]
            if origin_state_name not in states_names:
                state: State = State(name=str(origin_state_name))
                states_names.append(origin_state_name)
                self._states.add(state)
                if self._is_new_final_state(origin_state_name):
                    new_final_states.add(state)

            if destiny_state_name not in states_names:
                state: State = State(name=str(destiny_state_name))
                states_names.append(destiny_state_name)
                self._states.add(state)
                if self._is_new_final_state(destiny_state_name):
                    new_final_states.add(state)

            origin_state: State = self._get_state_by_name(str(origin_state_name))
            destiny_state: State = self._get_state_by_name(str(destiny_state_name))
            self._transitions.add(Transition(origin_state, transition[1], destiny_state))

        self._final_states = new_final_states

    def _get_state_by_name(self, name: str) -> Optional[State]:
        for state in self._states:
            if state.get_name() == name:
                return state

        return None

    def determinization(self) -> None:
        if ("&" not in self._symbols):
            return None

        e_closure = self._get_e_closure()

        new_states: List[Set[State]] = list(e_closure.values())
        self._symbols.remove("&")
        new_transitions = self._get_new_transitions(new_states, e_closure)
        self._set_new_states(new_transitions)
        self._initial_state = self._get_state_by_name(str(e_closure[self._initial_state]))

        return None

    def _get_new_transitions(self,
                             list_of_new_states: List[Set[State]],
                             e_closure: Dict[State, Set[State]]
                             ) -> List[Tuple[Set[State], str, Set[State]]]:
        new_transitions = []
        stack = list(list_of_new_states)
        while stack:
            new_states = stack.pop()
            for symbol in self._symbols:
                result_state: Set[State] = set()
                for state in new_states:
                    transition = self._get_transition(state, symbol)
                    if transition:
                        aux_state: State = transition.get_destiny_state()
                        aux_e_closure = e_closure[aux_state]
                        result_state |= aux_e_closure

                if result_state:
                    new_transitions.append((new_states, symbol, result_state))
                    if (result_state not in list_of_new_states):
                        stack.append(result_state)
                        list_of_new_states.append(result_state)

        return new_transitions

    def _is_new_final_state(self, set_of_old_states: Set[State]) -> bool:
        for state in set_of_old_states:
            if state in self._final_states:
                return True

        return False

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

    # TODO: renomear e trocar retorno para destiny_state
    def _get_transition(self, origin, symbol) -> Optional[Transition]:
        for transition in self._transitions:
            if origin == transition.get_origin_state() and symbol == transition.get_symbol():
                return transition

        return None

    def get_transition(self, origin: State, symbol: str, destiny: State) -> Optional[Transition]:
        for transition in self._transitions:
            if (origin == transition.get_origin_state()) and (symbol == transition.get_symbol()) \
                    and destiny == transition.get_destiny_state():
                return transition

        return None

    def contains_transition(self, origin: State, symbol: str, destiny: State) -> bool:
        for transition in self._transitions:
            if (origin == transition.get_origin_state()) and (symbol == transition.get_symbol()) \
                    and destiny == transition.get_destiny_state():
                return True

        return False

    def __repr__(self):
        """
        estados | a | b |
        -----------------
            A   | B | A |
            B   | B | B |
        """

        string = "\u03B4|"
        for symbol in sorted(self._symbols):
            string += f"{symbol}|"
        string += "\n"
        for state in sorted(self._states, key=State.get_name):
            string += f"{state}|"
            for symbol in sorted(self._symbols):
                transition = self._get_transition(state, symbol)
                if transition:
                    string += f"{transition.get_destiny_state()}|"
                else:
                    string += "-|"

            string += "\n"
        return string
