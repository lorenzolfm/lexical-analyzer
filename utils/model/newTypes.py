from typing import Dict

concat: str = "."
closure: str = "*"
union: str = "|"
optional: str = "?"
epsilon: str = "&"

operators = [concat, closure, union, optional]
precedence: Dict[str, int] = {union: 0, concat: 1, closure: 2, optional: 2}
