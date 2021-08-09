from typing import List

from .newTypes import precedence, closure, epsilon, operators


def setup_regex(regex: str) -> str:
    regex = remove_white_spaces(regex)
    regex = insert_concats(regex)
    regex = infix_to_postfix(regex)
    regex = add_ending(regex)
    return regex


def remove_white_spaces(regex: str) -> str:
    return regex.replace(" ", "")


def insert_concats(regex: str) -> str:
    n_concat: int = 0
    new_regex: str = regex
    previous: str = " "

    for i in range(len(regex)):
        current: str = regex[i]
        if needs_concat_symbol(previous, current):
            new_regex = add_concat_symbol_at_index(new_regex, i + n_concat)
            n_concat += 1
        previous = current

    return new_regex


def needs_concat_symbol(previous: str, current: str) -> bool:
    if previous == " ":
        return False
    else:
        return (previous not in operators + ["("] or previous in "*?)") and (current not in operators + [")"] or current == "(")
        # return (previous.isalnum() or previous in "*?)") and (current.isalnum() or current == "(")



def add_concat_symbol_at_index(regex: str, index: int) -> str:
    return regex[:index] + "." + regex[index:]


def add_ending(regex: str) -> str:
    return regex + "#."


def infix_to_postfix(infix: str) -> str:
    postfix: str = ""
    stack: List[str] = []

    for char in infix:
        if (char not in operators) and (char not in "()"):
            postfix += char
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        elif char == closure:
            postfix += char
        elif not stack:
            stack.append(char)
        elif (stack[-1] == "(") or (precedence[char] > precedence[stack[-1]]):
            stack.append(char)
        else:
            while stack and (precedence[char] < precedence[stack[-1]]):
                postfix += stack.pop()
            postfix += char

    while stack:
        postfix += stack.pop()

    return postfix
