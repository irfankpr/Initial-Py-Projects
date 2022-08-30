s = int(input("enter the size : "))
a1 = [[[] for i in range(s)] for i in range(s)]
a2 = [[[] for i in range(s)] for i in range(s)]
print("enter values to 1st array : ")
for i in range(s):
    for j in range(s):
        a1[i][j] = int(input())
print("enter values to 2nd array : ")
for i in range(s):
    for j in range(s):
        a2[i][j] = int(input())
print(a1)
print(a2)
for i in range(s):
    for j in range(s):
        a1[i][j] = a1[i][j] + a2[i][j]
print(".......after add..........\n", a1)
