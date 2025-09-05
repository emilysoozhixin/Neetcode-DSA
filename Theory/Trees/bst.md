## Binary Search Trees

- has sorted property   
    - every node in the left subtree is smaller than the root and every node in the right subtree is greater than the root

### Time Complexity
- If we have a **balanced binary tree**, our search algorithm will run in **O(log n)** time. 
    - Balanced binary tree means that the height of the left-subtree is equal to the height of the right-subtree, or there is a difference of 1

- In a balanced tree, we can eliminate half the nodes each time, which results in 
O(log n), for reasons we discussed in the merge sort and binary search lessons.

- In the worst case we have a **skewed tree**, where the height of the tree is equal to the number of nodes. In this case, the time complexity will be **O(n)**.
