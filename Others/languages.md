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
