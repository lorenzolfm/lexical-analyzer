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

        symbols = {'a', 'b'}
        transitions = {
            Transition(q0, 'a', q2),
            Transition(q0, 'b', q1),
            Transition(q1, 'a', q2),
            Transition(q1, 'b', q2),
            Transition(q2, 'a', q2),
            Transition(q2, 'b', q2)
        }

        initial_state = q0
        final_states = {q1}

        fa_0 = FiniteAutomata(
            states = {q0, q1, q2},
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )

        q3 = State("q3")
        q4 = State("q4")
        q5 = State("q5")

        symbols = {'a', 'b'}
        transitions = {
            Transition(q3, 'a', q4),
            Transition(q3, 'b', q5),
            Transition(q4, 'a', q5),
            Transition(q4, 'b', q5),
            Transition(q5, 'a', q5),
            Transition(q5, 'b', q5)
        }

        initial_state = q3
        final_states= {q4}

        fa_1 = FiniteAutomata(
            states = {q3, q4, q5},
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )

        actual = automata_union(fa_0, fa_1)
        self.assertEqual(actual.get_initial_state().get_name(), 'S')
        self.assertEqual(actual.get_final_states(), {q1, q4})
        # TODO: testar transições
        return None
