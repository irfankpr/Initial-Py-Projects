def getAry(s):
    print("Enter values to 1st array : ")
    for i in range(s):
        for j in range(s):
            arr1[i][j] = int(input())
    print("Enter values to 2nd array : ")
    for i in range(s):
        for j in range(s):
            arr2[i][j] = int(input())


def addAAry(s):
    for i in range(s):
        for j in range(s):
            arr1[i][j] = arr1[i][j] + arr2[i][j]


def disAry(s):
    for i in range(s):
        for j in range(s):
            print(arr1[i][j], end="\t")
        print()


s = int(input("enter the size of array : "))
arr1 = [[[] for i in range(s)] for i in range(s)]
arr2 = [[[] for i in range(s)] for i in range(s)]

getAry(s)
addAAry(s)
disAry(s)
