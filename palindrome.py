str = input("enter a tring : ")
l = len(str)
tmp=0
for i in range(int(l/2)):
    if str[i] != str[l-1 - i]:
        tmp = 1
if tmp != 1:
    print("it's palindrome")
else:
    print("It's not palindrome")
