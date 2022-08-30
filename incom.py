inc = float(input("Enter your annual income : "))
if inc <= 250000:
    print("Tou don't have to pay any tax")
elif inc <= 500000:
    print("You have to pay", (inc * 5) / 100, "Rupees as tax")
elif inc<= 1000000:
    print("You have to pay", (inc * 20) / 100, "Rupees as tax")
elif inc<= 5000000:
    print("You have to pay", (inc * 30) / 100, "Rupees as tax")
