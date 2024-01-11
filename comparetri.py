a = [5, 6, 7]
b = [3, 6, 10]
alice = 0
bob = 0
for i, j in zip(range(len(a)), range(len(b))):
        if a[i] > b[j]:
            alice += 1
        if a[i] < b[j]:
             bob += 1
        if a[i] == b[j]:
            alice += 0
            bob += 0
print(alice)
print(bob)