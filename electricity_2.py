def consumption():
    consumption = input("Enter the amount of kWh you consumed: ")
    return consumption

while True:
    #inputs the customer type
    customerType = input("Enter your customer type: ").upper()
    
    #computes the electricity bill for residential customer
    if customerType == "RESIDENTIAL":

        #electricity bill if the total consumption is less than or equal to 100
        while True:
            try:
                consumptionAmount = float(consumption())
                if consumptionAmount <= 100:
                    print("Customer Type: Residential")
                    print(f"Total number of consumption: {consumptionAmount} kWh")
                    print(f"Electricity bill: {10 * consumptionAmount} pesos")
                    break
                #electricity bill if the total consumption is greater than 100
                else:
                    print("Customer Type: Residential")
                    print(f"Total number of consumption: {consumptionAmount} kWh")
                    print(f"Electricity bill: {12 * consumptionAmount} pesos")
                    break
            except:
                print("Invalid input. Enter a numeric value.")
                continue

    #computes the electricity bill for commercial customer
    elif customerType == "COMMERCIAL":

        while True:
            try:
                consumptionAmount = float(consumption())
                #electricity bill if the total consumption is less than or equal to 500
                if consumptionAmount <= 500:
                    print("Customer Type: Commercial")
                    print(f"Total number of consumption: {consumptionAmount} kWh")
                    print(f"Electricity bill: {15 * consumptionAmount} pesos")
                    break

                #electricity bill if the total consumption is greater than 500
                else:
                    print("Customer Type: Commercial")
                    print(f"Total number of consumption: {consumptionAmount} kWh")
                    print(f"Electricity bill: {18 * consumptionAmount} pesos")
                    break
            except:
                print("Invalid input. Enter a numeric value.")
                continue
    
    #computes the electricity bill for industrial customer
    elif customerType == "INDUSTRIAL":
         while True:
            try:
                consumptionAmount = float(consumption())
                print("Customer Type: Industrial")
                print(f"Total number of consumption: {consumptionAmount} kWh")
                print(f"Electricity bill: {20 * consumptionAmount} pesos")
                break
            except:
                print("Invalid input. Enter a numeric value.")
                continue
    else:
        print("Invalid input.")
        continue
    break
