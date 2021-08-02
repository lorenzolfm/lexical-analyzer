from typing import Set, List

from .model.FiniteAutomata import FiniteAutomata
from .model.Transition import Transition
from .model.State import State


def automata_union(*automatas: FiniteAutomata) -> FiniteAutomata:
    states: Set[State] = set()
    symbols: Set[str] = set()
    final_states: Set[State] = set()
    transitions: Set[Transition] = set()
    initial_state: State = State("S")

    for automata in automatas:
        states |= automata.get_states()
        symbols |= automata.get_symbols()
        final_states += automata.get_final_states()

        new_transition = Transition(initial_state, "&", automata.get_initial_state())
        transitions.add(new_transition)
        transitions += automata.get_transitions()

    states: List[State] = list(states)
    symbols: List[str] = list(symbols)
    transitions: List[Transition] = list(transitions)
    final_states: List[State] = list(final_states)

    nfa = FiniteAutomata(states=states, symbols=symbols, transitions=transitions,
                         initial_state=initial_state, final_states=final_states)

    return nfa
