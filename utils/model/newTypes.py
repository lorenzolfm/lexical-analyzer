from typing import Dict

union: str = "|"
concat: str = "."
epsilon: str = "&"
closure: str = "*"
optional: str = "?"
end_of_sentence: str = "#"

operators = [concat, closure, union, optional]
precedence: Dict[str, int] = {union: 0, concat: 1, closure: 2, optional: 2}
