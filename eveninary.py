s = int(input("Enter the array size : "))
a = []
print("enter values to array : ")
count = 0
for i in range(s):
    n = int(input())
    a.append(n)
    if (n % 2 == 0):
        count = count + 1
print("Number of even numbers in array is : ", count)
