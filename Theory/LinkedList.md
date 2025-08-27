## Linked List
- A **linked list** is a linear data structure where elements (nodes) are stored at non-contiguous memory locations.
- Each node contains:
  1. **Data** (value)
  2. **Pointer(s)** to the next node (and/or previous node in case of doubly linked lists).
- Unlike arrays, linked lists do not require a fixed size at creation.
- **Dynamic** in nature – can grow/shrink at runtime.
- No direct indexing (must traverse from head).

---

## Singly Linked List
- Each node points to the **next** node.
- Last node’s `next` pointer is `null`.
- Traversal is one-directional.
- If the linked list is *empty*, the head (or head pointer) is usually set to None (in Python) or null (in Java, C#, etc.).

It *would not return 0* unless you explicitly coded it that way (e.g., initializing head as 0 instead of None).
    
### Node Structure (Example in C)
```c
struct Node {
    int data;
    struct Node* next;
};


