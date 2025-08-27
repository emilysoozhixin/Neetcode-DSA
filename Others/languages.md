## TYPING 
- Python is dynamically typed, meaning variables don’t have to declare a
```p
x = 5       # integer
x = "hello" # now a string
```
- Typing (type hints) is optional, but useful:
```p
from typing import List

def eat_sandwiches(arr: List[int]):
    print(arr)

eat_sandwiches([1, 2, 3])  # ✅ works
eat_sandwiches("hello")    # ❌ type checker will warn
```

### Arbitrary Precision in Python
- Arbitrary precision means that a number can grow as large as the memory allows, instead of being limited by a fixed number of bits.
- **Contrast with C++ / Java / C:**
    - C++ int (32-bit signed) range: -2,147,483,648 to 2,147,483,647
    - Java int (32-bit signed) same range