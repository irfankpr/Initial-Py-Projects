s = int(input("Enter the array size : "))
a = []
b = []

print("enter values to 1st array : ", end="")
for i in range(s):
    a.append(input())
print("enter values to 2st array : ")
for i in range(s):
    b.append(input())
print("array 1 :", a)
print("array 2 :", b)
# swapping
for i in range(s):
    tmp = a[i]
    a[i] = b[i]
    b[i] = tmp
print("...........After swapping......... ")
print(a)
print(b)
print("<<<<<<<<<<<<<<<<<main>>>>>>>>>>>>>>>>>>")
