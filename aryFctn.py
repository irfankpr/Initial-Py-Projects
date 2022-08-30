s = int(input("enter the size of array : "))
ary = [[[] for i in range(s)] for i in range(s)]


# Reads elements to array
def getAry():
    print("enter elements into array : ")
    for i in range(s):
        for j in range(s):
            ary[i][j] = int(input())


# display array
def disAry():
    print("the array is : ")
    for i in range(s):
        for j in range(s):
            print(ary[i][j], "\t", end="")
        print()


getAry()
disAry()
