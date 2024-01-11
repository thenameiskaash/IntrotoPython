nums = [1, 2, 3] #<---- O(1)
sum(nums)        #<---- O(n)
for n in nums:
    print(n)

#O(n) means worst case run time
#Both of these are also O(n) because they are being inserted and removed in the middle of an array
nums.insert(1,100)  #<---- O(n)
nums.remove(100)    #<---- O(n)
print(100 in nums) #Search  #<---- O(n)

