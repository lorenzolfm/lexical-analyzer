from utils.controller.Controller import Controller
from utils.model.AbstractSyntaxTree import AbstractSyntaxTree

if __name__ == "__main__":
    # app = Controller()
    # app.run()
    # #.*(b|a).a
    tree = AbstractSyntaxTree("a(a|b)*")

