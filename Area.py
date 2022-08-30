import sys


class Area():
    def cir(self):
        r = float(input("enter radius of circle : "))
        print("area of circle is : ", 3.14159 * r * r)

    def squ(self):
        l = float(input("enter side length : "))
        print("Area of square is : ", l * l)

    def tri(self):
        h = float(input("enter height of triangle : "))
        b = float(input("enter height of triangle : "))
        print("Area of triangle : ", (h * b) / 2)

    def ret(self):
        l = float(input("enter length : "))
        w = float(input("enter width : "))
        print("Area of rectangle is : ", l * w)


class MyCls(Area):
    ch = int(input("Choose : 1:Circle    2:Square    3:Triangle    4:Rectangle "))
    if ch < 1 or ch > 4:
        sys.exit("....... Invalid entry .........")


obj = MyCls()
List = [obj.cir, obj.squ, obj.tri, obj.ret]
List[obj.ch - 1]()
