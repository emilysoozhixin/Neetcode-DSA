## RAM 
- Also referred as memory
- has value and address
    - ![alt text](<../Images/Screenshot 2025-08-06 at 14.41.37.png>)
    - ![alt text](<../Images/Screenshot 2025-08-06 at 14.42.43.png>)
- Each byte have 8 bits 
- **Array** - An ordered collection of contiguous elements

## Static Array
- In statically typed languages like Java, C++ and C#, arrays must have an allocated size and type when initialized. These are known as static arrays.
- They are called **static** because the size of the array cannot change once declared. Once the array is full, it cannot store additional elements. 

### Key operations:

| Operation   | Time Complexity | Description                |
|-------------|----------------|----------------------------|
| Read        | O(1)           | Access an element by index |
| Insert      | O(n)           | Add an element (shifting may be needed) <br><sub>note: inserting at the end would be O(1)</sub>|
| Delete      | O(n)           | Remove an element (shifting may be needed) <br><sub>note: inserting at the end would be O(1)</sub>|
| Update      | O(1)           | Replace an element at a given index |

## Dynamic Array
- A **dynamic array** automatically resizes itself when it runs out of capacity.
- Common in high-level languages like Python (`list`), Java (`ArrayList`), and C++ (`vector`).
- When the array is full and a new element is added, the array:
  1. Allocates a new array with larger capacity (usually doubled).
  2. Copies existing elements to the new array.
  3. Inserts the new element.
- **Amortized (Average) Complexity**:  
  - Most insertions at the end are **O(1)**.  
  - When resizing is needed, it becomes **O(n)**, but this happens infrequently.

### Key operations:
| Operation   | Time Complexity   | Description                           |
|-------------|-------------------|---------------------------------------|
| Read        | O(1)             | Access an element by index           |
| Insert (end)| Amortized O(1)   | Add an element at the end            |
| Insert (mid)| O(n)             | Add an element at a specific index   |
| Delete      | O(n)             | Remove an element (shifting needed)  |
| Update      | O(1)             | Replace an element at a given index  |


## Stacks 
- one form of dynamic array
- LIFO data structure 
    - Use Case:
        - Reverse a sequence 
### Key operations:
| Operation   | Time Complexity | Description                       |
|-------------|----------------|-----------------------------------|
| Push        | O(1)           | Add an element to the top         |
| Pop         | O(1)           | Remove the top element            |
| Peek/Top    | O(1)           | View the top element without removing |
| IsEmpty     | O(1)           | Check if the stack is empty       |
