# Traverse a square grid 
nums = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(len(nums)):  #going through an array i (n)
    for j in range(len(nums[i])): #going through the i array (n), so the notation is O(n*n)
        print("Traverse a square gird", nums[i][j])
#Summation of (n^2)/2

# Get every pair of elements in array
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print("Get every pair of elements in array", nums[i], nums[j])

#Futhermore, insertion sorting is also a O(n^2) notation since you are inserting in the middle (n) times.

#O(n*m)
nums = [[1,2,3], [4,5,6]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print("O(n*m)", nums[i][j])


#O(n^3) 3-dimensional
#Get every triplet of elements in array
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            print("O(n^3)", nums[i], nums[j], nums[k])
