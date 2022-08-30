week = {
    1: "sunday",
    2: "monday",
    3: "tuesday",
    4: "wednesday",
    5: "thursday",
    6: "friday",
    7: "saturday"
}
day = int(input("enter the day index : "))
if 0 < day <= 7:
    print(week[day])
else:
    print("invalid index number")
