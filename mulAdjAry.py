s = int(input("Enter the limit of array : "))
ary1 = []
ary2 = []
print("enter", s, "elements : ")
for i in range(s):
    ary1.append(int(input()))
print("inputted array is: ", ary1)
for i in range(s-1):
    n=ary1[i]*ary1[i+1]
    ary2.append(n)
print("The multiplied array is :", ary2)
