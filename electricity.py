#Name: Irish B. De Guzman
#Date: November 13, 2025
#Title: Electricity Bill

#inputs the customer type
customerType = input("Enter your customer type: ").upper()

#inputs the amount of electricity consumed
consumption = int(input("Enter the amount of kWh you consumed: "))

#computes the electricity bill for residential customer
if customerType == "RESIDENTIAL":

    #electricity bill if the total consumption is less than or equal to 100
    if consumption <= 100:
        print("Customer Type: Residential")
        print(f"Total number of consumption: {consumption} kWh")
        print(f"Electricity bill: {10 * consumption} pesos")

    #electricity bill if the total consumption is greater than 100
    else:
        print("Customer Type: Residential")
        print(f"Total number of consumption: {consumption} kWh")
        print(f"Electricity bill: {12 * consumption} pesos")

#computes the electricity bill for commercial customer
elif customerType == "COMMERCIAL":

    #electricity bill if the total consumption is less than or equal to 500
    if consumption <= 500:
        print("Customer Type: Commercial")
        print(f"Total number of consumption: {consumption} kWh")
        print(f"Electricity bill: {15 * consumption} pesos")

    #electricity bill if the total consumption is greater than 500
    else:
        print("Customer Type: Commercial")
        print(f"Total number of consumption: {consumption} kWh")
        print(f"Electricity bill: {18 * consumption} pesos")

#computes the electricity bill for industrial customer
elif customerType == "INDUSTRIAL":
    print("Customer Type: Industrial")
    print(f"Total number of consumption: {consumption} kWh")
    print(f"Electricity bill: {20 * consumption} pesos")

else:
    print("Invalid input.")









