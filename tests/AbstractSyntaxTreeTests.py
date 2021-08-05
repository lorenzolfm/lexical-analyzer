import unittest

from utils.model.AbstractSyntaxTree import AbstractSyntaxTree


class AbstractSyntaxTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = AbstractSyntaxTree("ola")
        return None
