from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.nums = nums

    # def heapify(self, arr):
    #     # 0-th position is moved to the end
    #     arr.append(arr[0])

    #     self.heap = arr
    #     cur = (len(self.heap) - 1) // 2
    #     while cur > 0:
    #         # Percolate down
    #         i = cur
    #         while 2 * i < len(self.heap):
    #             if (2 * i + 1 < len(self.heap) and 
    #             self.heap[2 * i + 1] < self.heap[2 * i] and 
    #             self.heap[i] > self.heap[2 * i + 1]):
    #                 # Swap right child
    #                 tmp = self.heap[i]
    #                 self.heap[i] = self.heap[2 * i + 1]
    #                 self.heap[2 * i + 1] = tmp
    #                 i = 2 * i + 1
    #             elif self.heap[i] > self.heap[2 * i]:
    #                 # Swap left child
    #                 tmp = self.heap[i]
    #                 self.heap[i] = self.heap[2 * i]
    #                 self.heap[2 * i] = tmp
    #                 i = 2 * i
    #             else:
    #                 break
    #         cur -= 1
    #     print(f' After heapify: {self.heap}')

    def add(self, val: int) -> int:
        # self.heapify(self.nums)
        # print(f' Before add: {self.nums}')
        self.nums.append(val)
        self.nums.sort()
        
        res = []
        diff = len(self.nums) - self.k 
        res.append(self.nums[diff])
        print(f'res: {res}')

# Input:
input = KthLargest(3, [4, 5, 8, 2])
input.add(3)
input.add(5)
input.add(10)
input.add(9)
input.add(4)

# Output: [null, 4, 5, 5, 8, 8]