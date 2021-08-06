from typing import TypeVar, Dict

T = TypeVar("T")
concat: chr = "."
closure: chr = "*"
union: chr = "|"
optional: chr = "?"

operators = [concat, closure, union, optional]
precedence: Dict[chr, int] = {union: 0, concat: 1, closure: 2, optional: 2}
