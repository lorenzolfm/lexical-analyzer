from typing import Tuple, List

operators: str = "|?*."

# Testada
def setup_regex(regex: str) -> str:
    regex = remove_white_spaces(regex)
    regex = insert_concats(regex)
    regex = add_ending(regex)
    regex = reverse_regex(regex)
    regex = reorg_regex(regex)
    return regex

# Testada
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

# Testada
def needs_concat_symbol(previous: str, current: str) -> bool:
    return (previous.isalnum() or previous in "*?)") and (current.isalnum() or current == "(")

# Testada
def add_concat_symbol_at_index(regex: str, index: int) -> str:
    return regex[:index] + "." + regex[index:]

# Testada
def add_ending(regex: str) -> str:
    return regex + ".#"

# Testada
def reverse_regex(regex: str) -> str:
    regex_list = list(regex[::-1])

    for i in range(len(regex)):
        if regex_list[i] == "(":
            regex_list[i] = ")"
        elif regex_list[i] == ")":
            regex_list[i] = "("

    return "".join(regex_list)

def reorg_regex(regex: str) -> str:
    new_regex: str = ""
    operators: str = "|?*."
    i: int = 0

    while (i < len(regex) - 1):
        actual, next_ = regex[i], regex[i+1]
        if actual == "(":
            new_regex, i = reorg_subregex(regex, new_regex, i)
        elif (actual not in operators) and (next_ in operators):
            new_regex += next_ + actual
            i += 2
        elif (actual == "*"):
            new_regex += actual
            i += 1
        else:
            new_regex += actual + next_
            i += 1

    if "*" in new_regex:
        new_regex = closure_reorg(new_regex)
    if len(regex) != len(new_regex):
        new_regex += regex[-1]

    return new_regex

def reorg_subregex(regex: str, new_regex: str, index: int) -> Tuple[str, int]:
    substr: str = get_substr(regex, index + 1)
    subregex: str = "(" + reorg_regex(substr) + ")"
    index += len(subregex)

    if (index < len(regex)) and (regex[index] in operators):
        new_regex += regex[index]
        index += 1

    new_regex += subregex
    return new_regex, index

def closure_reorg(regex: str) -> str:
    new_regex: str = ""
    i: int = 0
    while (i < len(regex) - 1):
        actual = regex[i]
        next_ = regex[i+1]
        if actual == "*" and next_ in operators:
            new_regex += next_ + actual
            i += 2
        else:
            new_regex += actual
            i += 1

    if len(regex) != len(new_regex):
        new_regex += regex[-1]

    return new_regex

def get_substr(string: str, index: int) -> str:
    substring: str = ""
    stack: List[str] = ['(']
    while (stack):
        if string[index] == ")":
            stack.pop()
            if stack:
                substring += string[index]
        elif string[index] == "(":
            stack.append("(")
            substring += string[index]
        else:
            substring += string[index]
        index += 1

    return substring
