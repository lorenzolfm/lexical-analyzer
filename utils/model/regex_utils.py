from typing import List

from .newTypes import precedence, closure, epsilon, operators


def setup_regex(regex: str) -> str:
    regex = remove_white_spaces(regex)
    regex = insert_concats(regex)
    regex = infix_to_postfix(regex)
    regex = add_ending(regex)
    return regex


def replace_optional(regex: str) -> str:
    index: int = regex.find("?")
    # print(index)
    stack: List[str] = []
    while index != -1:
        char = regex[index - 1]
        if char == ")":
            stack.append(")")
            new_regex = ")?"
            index -= 1
            while stack:
                char = regex[index - 1]
                new_regex = char + new_regex
                if char == "(":
                    stack.pop()
                elif char == ")":
                    stack.append(char)

                index -= 1
        else:
            new_regex = char + "?"

        # print(new_regex, new_regex[:-1])
        regex = regex.replace(new_regex, "(" + new_regex[:-1] + "|&)")
        # print(regex)
        index = regex.find("?")
        # print(index)

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

def convert_regex_syntax(regex: str) -> str:
    regex = regex[1:-1]
    if regex[0].isalpha():
        new_regex = convert_alpha_regex(regex)
    else:
        new_regex = convert_num_regex(regex)

    new_regex = "(" + new_regex + ")*"
    return new_regex

def convert_alpha_regex(regex: str) -> str:
    new_regex: str = ""
    alpha_list = []

    for i in range(0, len(regex), 3):
        alpha_list.append([regex[i], regex[i+2]])

    for sublist in alpha_list:
        begin_char = ord(sublist[0])
        end_char = ord(sublist[-1])

        for i in range(begin_char, end_char + 1):
            new_regex += chr(i)
            new_regex += "|" if i != end_char else ""

        if sublist != alpha_list[-1]:
            new_regex += "|"

    return new_regex

def convert_num_regex(regex: str) -> str:
    new_regex: str = ""
    begin_num = int(regex[0])
    end_num = int(regex[-1])
    for i in range(begin_num, end_num + 1):
        new_regex += str(i)
        new_regex += "|" if i != end_num else ""

    return new_regex
