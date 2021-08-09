import unittest

from utils.model.FiniteAutomata import FiniteAutomata
from utils.model.Transition import Transition
from utils.model.State import State

from utils.algorithm import automata_union

class AlgorithmTest(unittest.TestCase):
    def test_automata_union(self) -> None:
        q0 = State("q0")
        q1 = State("q1")
        q2 = State("q2")

        states_0 = {q0, q1, q2}

        symbols_0 = {'a', 'b'}
        transitions_0 = {
            Transition(q0, 'a', q2),
            Transition(q0, 'b', q1),
            Transition(q1, 'a', q2),
            Transition(q1, 'b', q2),
            Transition(q2, 'a', q2),
            Transition(q2, 'b', q2)
        }

        initial_state_0 = q0
        final_states_0 = {q1}

        fa_0 = FiniteAutomata(
            states = states_0,
            symbols = symbols_0,
            transitions = transitions_0,
            initial_state = initial_state_0,
            final_states = final_states_0
        )

        q3 = State("q3")
        q4 = State("q4")
        q5 = State("q5")

        states_1 = {q3, q4, q5}

        symbols_1 = {'a', 'b'}
        transitions_1 = {
            Transition(q3, 'a', q4),
            Transition(q3, 'b', q5),
            Transition(q4, 'a', q5),
            Transition(q4, 'b', q5),
            Transition(q5, 'a', q5),
            Transition(q5, 'b', q5)
        }

        initial_state_1 = q3
        final_states_1 = {q4}

        fa_1 = FiniteAutomata(
            states = states_1,
            symbols = symbols_1,
            transitions = transitions_1,
            initial_state = initial_state_1,
            final_states = final_states_1
        )

        actual: FiniteAutomata = automata_union(fa_0, fa_1)
        initial_state: State = actual.get_initial_state()
        self.assertEqual(initial_state.get_name(), 'S')
        self.assertEqual(actual.get_final_states(), final_states_0 | final_states_1)
        self.assertEqual(actual.get_states(), states_0 | states_1 | {initial_state})
        self.assertEqual(actual.get_symbols(), symbols_0 | symbols_1 | {"&"})
        self.assertTrue(actual.contains_transition(initial_state, "&", initial_state_0))
        self.assertTrue(actual.contains_transition(initial_state, "&", initial_state_1))
        transition_0 = actual.get_transition(initial_state, "&", initial_state_0)
        transition_1 = actual.get_transition(initial_state, "&", initial_state_1)
        self.assertEqual(actual.get_transitions(), {transition_0, transition_1} | transitions_0 | transitions_1)

        return None
