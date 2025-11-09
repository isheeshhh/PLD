loopRange = int(input("Enter number: "))
while True:
    choice = input("Enter a letter: ").capitalize()

    if choice == "A":
        for i in range(loopRange):
            print("*" * i)
        for i in range(loopRange, 0, -1):
            print("*" * i)
        break 
    elif choice == "B":
        for i in range(loopRange):
            print(" " * ((loopRange - 1) - i) + "*" * i)
        for i in range((loopRange - 2), -1, -1):
            print(" " * ((loopRange - 1) - i) + "*" * i)
        break
    elif choice == "C":
        for i in range(loopRange):
            print(("*" * i) + (" " * ((loopRange - 1) - i)) + (" " * ((loopRange - 1) - i)) + ("*" * i))
        for i in range((loopRange - 2), -1, -1):
            print(("*" * i) + (" " * ((loopRange - 1) - i)) + (" " * ((loopRange - 1) - i)) + ("*" * i))
        break
    else: 
        print("Invalid input!")