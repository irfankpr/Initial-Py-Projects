num = int(input("Enter the number > 1 : "))
flg = True
for i in range(2, num):
    if num % i == 0:
        print("It's not prime")
        flg = False
        break
if flg:
    print("The number is prime ")
