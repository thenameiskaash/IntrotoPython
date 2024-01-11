#O(logN) is used on Binary Search for example
def search(root, target):
    if not root:
        return False
    if target < root:
        return search(root.left,target)
    elif target > root:
        return search(root.right, target)
    else:
        return True
    
#How many times can you cut the value (n) by 2 until it equals 1?
#How many times can you take the value 1 and multiple by 2 until you reach n?
#2^x = n? === x = log(n)

#O(nlogn)
#HeapSort
import heapq
nums = [1,2,3,4,5]      #O(n)
heapq.heapify(nums)     #O(n)
while nums:
    heapq.heappop(nums) #O(logn)

#MergeSort is another example of O(nlogn)
#Along with most built-in sorting functions