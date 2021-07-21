from typing import List, Set, Dict, Tuple, Optional

# For simple built-in types, just use the name of the type
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

# For collections, the type of the collection item is in brackets
# (Python 3.9+)
x: list[int] = [1]
x: set[int] = {6, 7}

# In Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from 'typing'
x: List[int] = [1]
x: Set[int] = {6, 7}

# Same as above, but with type comment syntax (Python 3.5 and earlier)
x = [1]  # type: List[int]

# For mappings, we need the types of both keys and values
x: dict[str, float] = {'field': 2.0}  # Python 3.9+
x: Dict[str, float] = {'field': 2.0}

# For tuples of fixed size, we specify the types of all the elements
x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+
x: Tuple[int, str, float] = (3, "yes", 7.5)

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+
x: Tuple[int, ...] = (1, 2, 3)

# Use Optional[] for values that could be None
x: Optional[str] = some_function()
# Mypy understands a value can't be None in an if-statement
if x is not None:
    print(x.upper())
# If a value can never be None due to some invariants, use an assert
assert x is not None
print(x.upper())