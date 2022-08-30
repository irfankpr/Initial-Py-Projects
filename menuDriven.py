print("1:ADD   2:SUB    3:MUL    4:DIV")
ch = int(input("Enter your choice : "))
if 0 < ch < 5:
    n1 = int(input("Enter 2 numbers :"))
    n2 = int(input())

    def add():
        print("sum of", n1, "and", n2, "is", n1 + n2)


    def sub():
        print("difference of", n1, "and", n2, "is", n1 - n2)


    def mul():
        print("product of", n1, "and", n2, "is", n1 * n2)


    def div():
        print("quotient of", n1, "and", n2, "is", n1 / n2)


    opr = [add, sub, mul, div]
    opr[ch-1]()
else:
    print("invalid input")
