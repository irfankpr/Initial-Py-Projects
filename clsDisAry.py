class AryP:
    @staticmethod
    def getAry(s):
        print("Enter values to 1st array : ")
        for i in range(s):
            for j in range(s):
                arr[i][j] = int(input())

    @staticmethod
    def disAry(s):
        for i in range(s):
            for j in range(s):
                print(arr[i][j], end="\t")
            print()


s = int(input("Enter the size of array : "))
arr = [[[] for i in range(s)] for i in range(s)]
obj = AryP()
obj.getAry(s)
obj.disAry(s)
