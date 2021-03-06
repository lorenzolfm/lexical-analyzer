from typing import Set, List

from .model.FiniteAutomata import FiniteAutomata
from .model.Transition import Transition
from .model.State import State


def get_key_by_value(dict_: dict, data):
    """

    Args:
        dict_: Generic dictionary.
        data: value of the dictionary.

    Returns:
        Key of the data.
    """
    for key, value in dict_.items():
        if value == data:
            return key

    return None


def automata_union(automatas: List[FiniteAutomata]) -> FiniteAutomata:
    """

    Args:
        automatas: list of finite automata.

    Returns:
        One finite automata.

    """
    if len(automatas) == 1:
        return automatas[0]

    initial_state: State = State("S")
    states: Set[State] = {initial_state}
    symbols: Set[str] = set()
    final_states: Set[State] = set()
    transitions: Set[Transition] = set()

    for automata in automatas:
        states |= automata.get_states()
        symbols |= automata.get_symbols()
        final_states |= automata.get_final_states()

        new_transition = Transition(initial_state, "&", automata.get_initial_state())
        transitions.add(new_transition)
        transitions |= automata.get_transitions()

    nfa = FiniteAutomata(states=states, symbols=symbols.union({'&'}), transitions=transitions,
                         initial_state=initial_state, final_states=final_states)

    return nfa
