alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**3]
print(alist[0](10), alist[1](2,2))
print("Using lambda function : ", alist[2](3))

key = 'm'
aDict = {'m' : lambda x:x*2, 'n' : lambda x:x*3}
print("lambda function with dictionary", aDict[key](9))

string = "Hello"
upper = lambda string: string.upper()
print("lambda with strings : ", upper(string))

max = lambda a, b : a if (a>b) else b
print(max(1,2))


def even_numbers(nums):
    even_list = []
    for i in nums:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

listing = [0,12,34,54,63,78,32]
print("even numbers normally : ", even_numbers(listing))

even_nums = list(filter(lambda x: x % 2 == 0, listing))
print("even numbers using lambda : ", even_nums)


List = [[4,3,2], [16,4,66,1], [12,6,9,3]]

sortlist = lambda x: (sorted(i) for i in x)
print("Sorted of given list : ", list(sortlist(List)))

secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortlist)
print("Second largest value", res)
