s = int(input("Enter the array size : "))
a = []
for i in range(s):
    n = int(input())
    a.append(n)
for i in range(s):
    for j in range(s):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a)
