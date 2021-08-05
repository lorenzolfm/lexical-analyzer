from utils.controller.Controller import Controller
from utils.model.AbstractSyntaxTree import AbstractSyntaxTree, construct_tree

if __name__ == "__main__":
    # app = Controller()
    # app.run()
    # #.*(b|a).a
    # tree = AbstractSyntaxTree("a(a|b)*")
    # tree = construct_tree("a(a|b)*")
    # .#.*(.*(|ba)a)a
    tree = construct_tree("a(a(a|b)*)*")
    tree = construct_tree("(a|b)*abb")
