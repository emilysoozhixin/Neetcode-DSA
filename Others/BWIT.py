# # ########### ARRAY AND LINKED LIST ###########
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# # def reverse_linked_list(head):
# #     prev = None
# #     current = head
# #     while current is not None:
# #         next_node = current.next
# #         current.next = prev
# #         prev = current
# #         current = next_node
# #     return prev

# # def reverse_array(arr):
# #     left = 0
# #     right = len(arr) - 1
# #     while left < right:
# #         arr[left], arr[right] = arr[right], arr[left]
# #         left += 1
# #         right -= 1
# #     return arr

# # def print_list(head):
# #     current = head
# #     while current is not None:
# #         print(current.value, end=" -> ")
# #         current = current.next
# #     print("NULL")

# # def next_term(s):
# #     res = []
# #     i = 0 
# #     while i < len(s):
# #         count = 1
# #         while i + 1 < len(s) and s[i] == s[i + 1]:
# #             i += 1
# #             count += 1
# #         res.append(str(count) + s[i])
# #         i += 1
# #     return ''.join(res) 


# # def look_and_say(n):
# #     curr = '1'
# #     seq = [curr]
# #     for _ in range(1, n):
# #         curr = next_term(curr)
# #         seq.append(curr)
# #     return seq

# # def main():
# #     ############Exercise 3: Reverse an array
# #     # O(1): This algorithm swaps elements in place, meaning it does not require any additional space that grows with the input size. 
# #     # O(n): This algorithm has a time complexity of O(n) because it iterates through the entire array once to reverse it.
# #     user_input = input("Enter a list of numbers separated by commas (e.g., 1,2,3): ")
# #     arr = [int(x.strip()) for x in user_input.split(",")]
# #     print(reverse_array(arr))

# #     ############ Exercise 4: Reverse a linked list
# #     user_input = input("Enter a list of numbers separated by commas for linked list (e.g., 1,2,3): ")
# #     numbers = [int(x.strip()) for x in user_input.split(",")]

# #     # Creating the linked list from user input
# #     head = ListNode(numbers[0])
# #     current = head
# #     for number in numbers[1:]:
# #         current.next = ListNode(number)
# #         current = current.next

# #     print("Original Linked List:")
# #     print_list(head)

# #     # Reversing the linked list
# #     reversed_head = reverse_linked_list(head)

# #     print("Reversed Linked List:")
# #     print_list(reversed_head)

# #     ############ Exercise 5: Look and Say
# #     # O(2^n): The time complexity of this algorithm is O(2^n) because the length of the string doubles with each iteration.
# #     n = int(input())
# #     if n <= 0:
# #         print("Invalid input")
# #         return
# #     sequence = look_and_say(n)
# #     for i, term in enumerate(sequence):
# #         print(f"Term {i + 1}: {term}")

# # if __name__ == "__main__":
# #     main()


# ########### HASH TABLE (3) ###########
# def has_majority(collection):
#     counts = {}
#     for item in collection:
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1

#     for item, count in counts.items():
#         if count > len(collection) // 2:
#             return item
#     return None

# user_input = [int(x.strip()) for x in input().split(",")]
# majority = has_majority(user_input)
# if majority:
#     print(majority)
# else:
#     print("-1")

# ########### HASH TABLE (4) ###########
# def deep_copy(head):
#     if not head:
#         return None

#     # Create a new head for the copied list
#     new_head = ListNode(head.value)
#     current_old_list = head.next
#     current_new_list = new_head

#     # Copy each node and link them in the new list
#     while current_old_list:
#         new_node = ListNode(current_old_list.value)
#         current_new_list.next = new_node
        
#         # Move to the next node
#         current_new_list = new_node
#         current_old_list = current_old_list.next

#     return new_head


import re

def count_unique(input_list):
    unique = set()

    for word in input_list:
        word = word.strip().lower()
        if word:
            unique.add(word)

    return len(unique)

input_text = """
But, soft! what light through yonder window breaks?
It is the east, and Juliet is the sun.
Arise, fair sun, and kill the envious moon,
Who is already sick and pale with grief,
That thou her maid art far more fair than she:
Be not her maid, since she is envious;
Her vestal livery is but sick and green
And none but fools do wear it; cast it off.
It is my lady, O, it is my love!
O, that she knew she were!
She speaks yet she says nothing: what of that?
Her eye discourses; I will answer it.
I am too bold, 'tis not to me she speaks:
Two of the fairest stars in all the heaven,
Having some business, do entreat her eyes
To twinkle in their spheres till they return.
What if her eyes were there, they in her head?
"""

monologue = re.split(r'[.,;:!?]+\s*', input_text)
print(count_unique(monologue))