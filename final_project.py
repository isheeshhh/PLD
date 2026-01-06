#Name: Irish B. De Guzman
#Date: January 6, 2026
#Title: Final Project - Compilation of Exercises

def exercise_1():
    #Name: Irish B. De Guzman
    #Date: October 16, 2025
    #Title: Exercise 1 - Tree
    
    print ("\n\n\t\t\t\t\t\tI\n\t\t\t\t\t\t\b\bThink\n\t\t\t\t\t\t\b\b\b\b\bThat I shall\n\t\t\t\t\t\t\b\b\b\b\b\b\bNever see a poem\n\t\t\t\t\t\bAs lovely as a tree,\n\t\t\t\t\t\b\b\b\bA tree whose hungry mouth\n\t\t\t\t\t\b\b\b\b\b\bIs pressed against the earth's\n\t\t\t\t\t\b\b\b\b\b\b\b\bSweet flowing breast, a tree that\n\t\t\t\t\bLooks at God all day, and lifts it's\n\t\t\t\t\b\bLeafy arms to pray. A tree that may in\n\t\t\t\t\b\b\bSummer wear, a nest of robin in her hair;\n\t\t\t\t\b\b\b\b\b\bUpon whose bosom snow has lain; who intimately\n\t\t\t\t\t\t\b\b\b\b\b\b\bLives with rain\n\t\t\t\t\tPoems are made by\n\t\t\t\t\t\t\b\b\b\b\b\bFools like me\n\t\t\t\t\t\t\b\bBut\n\t\t\t\t\t\t\b\bOnly\n\t\t\t\t\t\t\b\bGod\n\t\t\t\t\t\t\b\bCan\n\t\t\t\t\t\t\b\bMake\n\t\t\t\t\t\t\bA\n\t\t\t\t\t\t\b\bTree\n\t\t\t\t\t\t\b\b\b\b\b\bJOYCE KILMER")
def exercise_2():
    #Name: Irish B. De Guzman
    #Date: October 25, 2025
    #Title: Exercise 2 - Receipt

    print("<<<<<<<<<<<<<<<< FINE DINING SNACK BAR >>>>>>>>>>>>>>>\n\n\t\t\t\b\b\bMenu for Today\n")
    print("Hot Dog\t\t\t\t\t\bPhp 45.50\nHamburger\t\t\t\t\t\b\b\b\b\b35.75\nFrench Fries\t\t\t\t\t\b\b\b\b\b25.85\nMilk Shake\t\t\t\t\t\b\b\b\b\b15.75\n")
    print("--------------------------------------------------------")
    #input the quantity per item
    hotdog = int(input("Enter quantity of Hot Dog: "))
    hamburger = int(input("Enter quantity of Hamburger: "))
    frenchFries = int(input("Enter quantity of French Fries: "))
    milkShake = int(input("Enter quantity of Milk Shake: "))

    #multiplies the price and quantity per item
    total_hotdog = 45.50 * hotdog
    total_hamburger = 35.75 * hamburger
    total_frenchFries = 25.85 * frenchFries
    total_milkShake = 15.75 * milkShake

    #rounds off the total price per item to the nearest hundreths
    roundedTotalHotdog = round(total_hotdog, 2)
    roundedTotalHamburger = round(total_hamburger, 2)
    roundedTotalFrenchFries = round(total_frenchFries, 2)
    roundedTotalMilkShake = round(total_milkShake, 2)

    #calculates the gross price
    grossPrice = roundedTotalHotdog + roundedTotalHamburger + roundedTotalFrenchFries + roundedTotalMilkShake

    #rounds off the gross price to the nearest hundreths
    roundedGrossPrice = round(grossPrice, 2)

    #calculates the VAT
    vat = roundedGrossPrice * 0.2

    #rounds off the VAT to the nearest hundreths
    roundedVat = round(vat, 2)

    #calculates the total price
    totalPrice = roundedGrossPrice + roundedVat

    #rounds off the total price to the nearest hundreths   
    roundedTotalPrice = round(totalPrice, 2)

    #calculates the total number of items sold
    numberOfItemsSold = hotdog + hamburger + frenchFries + milkShake
    print("\n\n<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    #outputs the quantity and price per item
    print(f"Hotdog\t\t\tPhp 45.50 x {hotdog} = Php {roundedTotalHotdog}")
    print(f"Hamburger\t\tPhp 35.75 x {hamburger} = Php {roundedTotalHamburger}")
    print(f"French Fries\t\tPhp 25.85 x {frenchFries} = Php {roundedTotalFrenchFries}")
    print(f"Milk Shake\t\tPhp 15.75 x {milkShake} = Php {roundedTotalMilkShake} \n\n")

    #outputs the gross price
    print(f"Gross Price\t\t\t\t\b\b\b = Php {roundedGrossPrice}")

    #outputs the VAT
    print(f"(w/VAT)\t\t\t\t\t\b\b\b = Php {roundedVat}")

    #outputs the total price
    print(f"Total Price\t\t\t\t\b\b\b = Php {roundedTotalPrice}\n")

    #inputs the amount tendered
    amountTendered = float(input("Enter amount tendered: "))

    #calculates the change
    change = amountTendered - totalPrice

    #rounds off the change to nearest hundreths
    roundedChange = round(change, 2)

    #outputs the amount tendered
    print(f"Amount Tendered\t\t\t\t\b\b\b = Php {amountTendered}")

    #outputs the change
    print(f"Your change is\t\t\t\t\b\b\b = Php {roundedChange}")

    print("\t\t\t\t\t\b\bvvvvvvvvvvvv")

    #outputs the total number of items sold
    print(f"Number of items sold: {numberOfItemsSold} items\n")

    print("************** THANK YOU AND COME AGAIN **************")
def exercise_3():
    #Name: Irish B De Guzman
    #Date: November 4, 2025
    #Title: Exercise 3 - Grades Computation

    #funtion for computing the percentage and weighted score
    def grades_computation(activity_name, percentage_str, percentage_int):
        #initializes the perfect score to 100
        perfect_score = 100
        #inputs the grade
        activity_grade = int(input(f"Enter your {activity_name} grade ({percentage_str}): "))
        #computes the percentage score
        activity_Ps = (activity_grade / perfect_score) * 100
        #computes the weighted score
        activity_Ws = activity_Ps * percentage_int
        return activity_Ps, activity_Ws

    print("Welcome to Grades Computation\n")
    print("\nClass Standing (Lecture) 70%\n")

    lecAssPs, lecAssWs = grades_computation("assignment", "15%", 0.15)
    lecProjPs, lecProjWs = grades_computation("project", "20%", 0.20)
    lecRecitPs, lecRecitWs = grades_computation("recitation", "10%", 0.10)
    lecQuizPs, lecQuizWs = grades_computation("quiz", "25%", 0.25)

    print("\nExamination (Lecture) 30%\n")

    lecExamPs, lecExamWs = grades_computation("examination", "30%", 0.30)

    print("\nClass Standing (Laboratory) 70%\n")
    labAssPs, labAssWs = grades_computation("assignment", "15%", 0.15)
    labProjPs, labProjWs = grades_computation("project", "20%", 0.20)
    labRecitPs, labRecitWs = grades_computation("recitation", "10%", 0.10)
    labQuizPs, labQuizWs = grades_computation("quiz", "25%", 0.25)

    print("\nExamination (Laboratory) 30%\n")
    labExamPs, labExamWs = grades_computation("examination", "30%", 0.30)

    #total of class standing (lecture) grade
    lecTotalCs = (lecAssWs + lecProjWs + lecRecitWs + lecQuizWs) 

    #computes the final (lecture) grade
    finalLecture = lecExamWs + lecTotalCs

    #total of class standing (lab) grade
    labTotalCs = (labAssWs + labProjWs + labRecitWs + labQuizWs) 

    #computes the final (lab) grade
    finalLab = labExamWs + labTotalCs

    #computes the final grade
    finalGrade = (finalLecture * 0.70) + (finalLab * 0.30)

    #rounds off the final grade to the nearest hundreths
    roundedFinalGrade = round(finalGrade, 2)

    #rounds up or rounds down the final grade
    integer_part = int(roundedFinalGrade)
    decimal_part = round(roundedFinalGrade - integer_part, 2)

    if decimal_part >= 0.50:
        roundFinalGrade = integer_part + 1
    else:
        roundFinalGrade = integer_part

    print("Final lecture: ", finalLecture)
    print("Final lab: ", finalLab)

    #outputs the final grade and remarks
    if roundFinalGrade >= 75:
        print(f"Your final grade is {roundedFinalGrade}. You passed!")
    else:
        print(f"Your final grade is {roundedFinalGrade}. You failed!")
def exercise_4():
    #Name: Irish B De Guzman
    #Date: November 4, 2025
    #Title: Exercise 4 - Grades Computation

    #funtion for computing the percentage and weighted score
    def grades_computation(activity_name, percentage_str, percentage_int):
        #initializes the perfect score to 100
        perfect_score = 100
        #inputs the grade
        activity_grade = int(input(f"Enter your {activity_name} grade ({percentage_str}): "))
        #computes the percentage score
        activity_Ps = (activity_grade / perfect_score) * 100
        #computes the weighted score
        activity_Ws = activity_Ps * percentage_int
        return activity_Ps, activity_Ws

    print("Welcome to Grades Computation\n")
    print("\nClass Standing (Lecture) 70%\n")

    lecAssPs, lecAssWs = grades_computation("assignment", "15%", 0.15)
    lecProjPs, lecProjWs = grades_computation("project", "20%", 0.20)
    lecRecitPs, lecRecitWs = grades_computation("recitation", "10%", 0.10)
    lecQuizPs, lecQuizWs = grades_computation("quiz", "25%", 0.25)

    print("\nExamination (Lecture) 30%\n")

    lecExamPs, lecExamWs = grades_computation("examination", "30%", 0.30)

    print("\nClass Standing (Laboratory) 70%\n")
    labAssPs, labAssWs = grades_computation("assignment", "15%", 0.15)
    labProjPs, labProjWs = grades_computation("project", "20%", 0.20)
    labRecitPs, labRecitWs = grades_computation("recitation", "10%", 0.10)
    labQuizPs, labQuizWs = grades_computation("quiz", "25%", 0.25)

    print("\nExamination (Laboratory) 30%\n")
    labExamPs, labExamWs = grades_computation("examination", "30%", 0.30)

    #total of class standing (lecture) grade
    lecTotalCs = (lecAssWs + lecProjWs + lecRecitWs + lecQuizWs) 

    #computes the final (lecture) grade
    finalLecture = lecExamWs + lecTotalCs

    #total of class standing (lab) grade
    labTotalCs = (labAssWs + labProjWs + labRecitWs + labQuizWs) 

    #computes the final (lab) grade
    finalLab = labExamWs + labTotalCs

    #computes the final grade
    finalGrade = (finalLecture * 0.70) + (finalLab * 0.30)

    #rounds off the final grade to the nearest hundreths
    roundedFinalGrade = round(finalGrade, 2)

    #rounds up or rounds down the final grade
    integer_part = int(roundedFinalGrade)
    decimal_part = round(roundedFinalGrade - integer_part, 2)

    if decimal_part >= 0.50:
        roundFinalGrade = integer_part + 1
    else:
        roundFinalGrade = integer_part

    print(f"Final lecture: {finalLecture}")
    print(f"Final lab:  {finalLab}")

    #outputs the final grade and remarks
    if roundFinalGrade >= 97 and roundFinalGrade <= 100:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.00. You Passed!")
    elif roundFinalGrade >= 94 and roundFinalGrade <= 96:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.25. You Passed!")
    elif roundFinalGrade >= 91 and roundFinalGrade <= 93:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.50. You Passed!")
    elif roundFinalGrade >= 88 and roundFinalGrade <= 90:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.75. You Passed!")
    elif roundFinalGrade >= 85 and roundFinalGrade <= 87:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.00. You Passed!")
    elif roundFinalGrade >= 82 and roundFinalGrade <= 84:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.25. You Passed!")
    elif roundFinalGrade >= 79 and roundFinalGrade <= 81:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.50. You Passed!")
    elif roundFinalGrade >= 76 and roundFinalGrade <= 78:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.75. You Passed!")
    elif roundFinalGrade == 75:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 3.00. You Passed!")
    else:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 5.00. You Failed!")
def exercise_5():
    #Name: Irish B. De Guzman
    #Date: November 13, 2025
    #Title: Exercise 5 - Grades Computation

    #function for computing grades
    def grades_computation(activity_name, percentage):
        activity_list = []
        activity_num = 0

        while True:
            #inputs the number of activities
            activity_getNum = input(f"Enter the number of {activity_name}: ")
            try:
                activity_getNum_int = int(activity_getNum)
                break
            except:
                print("Invalid input.")
                continue

        #loop that gets the scores
        while len(activity_list) < (activity_getNum_int):
            activity_num += 1
            activity_list.append(None)
            activity_getScore = input(f"Enter your grade in {activity_name} {activity_num}: ")
            
            try:
                activity_score = int(activity_getScore)
                activity_list[-1] = activity_score

            except:
                print("Invalid input.")
                activity_list.pop()
                activity_num -= 1
                continue

        #computes the total of scores
        activity_total = sum(activity_list)

        #computes the percentage score
        activity_PS = (activity_total / (activity_getNum_int * 100)) * 100

        #computes the weighted score
        activity_WS = activity_PS * percentage
        return activity_list, activity_PS, activity_WS

    #function for printing grades
    def print_grades(activity_name, catergory_name, list_name):
        print(f"{activity_name} ({catergory_name})")
        for index, items in enumerate(list_name):
            print(f"{activity_name} {index + 1} = {items}")
        print("------------------------------------")

    print("Grades Computation")
    
    print("\nLecture\n")

    print("Assignment\n")
    lecAssList, lecAssPs, lecAssWs = grades_computation("Assignment", 0.15)
    print("\nProject\n")
    lecProjList, lecProjPs, lecProjWs = grades_computation("Project", 0.20) 
    print("\nRecitation\n")
    lecRecitList, lecRecitPs, lecRecitWs = grades_computation("Recitation", 0.10) 
    print("\nQuiz\n")
    lecQuizList, lecQuizPs, lecQuizWs = grades_computation("Quiz", 0.25) 
    print("\nExamination\n")
    lecExamList, lecExamPs, lecExamWs = grades_computation("Examination", 0.30) 

    print("\nLaboratory\n")

    print("Assignment\n")
    labAssList, labAssPs, labAssWs = grades_computation("Assignment", 0.15)
    print("\nProject\n")
    labProjList, labProjPs, labProjWs = grades_computation("Project", 0.20) 
    print("\nRecitation\n")
    labRecitList, labRecitPs, labRecitWs = grades_computation("Recitation", 0.10) 
    print("\nQuiz\n")
    labQuizList, labQuizPs, labQuizWs = grades_computation("Quiz", 0.25) 
    print("\nExamination\n")
    labExamList, labExamPs, labExamWs = grades_computation("Examination", 0.30) 

    #computes the final grade for lecture
    finalLec = lecAssWs + lecProjWs + lecRecitWs + lecQuizWs + lecExamWs

    #computes the final grade for laboratory
    finalLab = labAssWs + labProjWs + labRecitWs + labQuizWs + labExamWs

    #computes the final grade
    finalGrade = (finalLec * 0.70) + (finalLab * 0.30)

    #rounds off the final grade to the nearest hundreths
    roundedFinalGrade = round(finalGrade, 2)

    #rounds up or rounds down the final grade
    integer = int(roundedFinalGrade)

    if roundedFinalGrade > integer:
        roundFinalGrade = integer + 1
    else:
        roundFinalGrade = integer

    print("\n")
    lecAssPrint = print_grades("Assignement","Lecture", lecAssList)
    lecProjPrint = print_grades("Project","Lecture", lecProjList)
    lecRecitPrint = print_grades("Recitation","Lecture", lecRecitList)
    lecQuizPrint = print_grades("Quiz","Lecture", lecQuizList)
    lecExamPrint = print_grades("Examination","Lecture", lecExamList)

    labAssPrint = print_grades("Assignement","Laboratory", labAssList)
    labProjPrint = print_grades("Project","Laboratory", labProjList)
    labRecitPrint = print_grades("Recitation","Laboratory", labRecitList)
    labQuizPrint = print_grades("Quiz","Laboratory", labQuizList)
    labExamPrint = print_grades("Examination","Laboratory", labExamList)

    print(f"Final Lecture: {finalLec}")
    print(f"Final Lab: {finalLab}")
    print(f"Rounded Final Grade (int): {roundFinalGrade} \n")

    #outputs the final grade and remarks
    if roundFinalGrade >= 97 and roundFinalGrade <= 100:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.00. You Passed!")
    elif roundFinalGrade >= 94 and roundFinalGrade <= 96:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.25. You Passed!")
    elif roundFinalGrade >= 91 and roundFinalGrade <= 93:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.50. You Passed!")
    elif roundFinalGrade >= 88 and roundFinalGrade <= 90:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.75. You Passed!")
    elif roundFinalGrade >= 85 and roundFinalGrade <= 87:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.00. You Passed!")
    elif roundFinalGrade >= 82 and roundFinalGrade <= 84:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.25. You Passed!")
    elif roundFinalGrade >= 79 and roundFinalGrade <= 81:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.50. You Passed!")
    elif roundFinalGrade >= 76 and roundFinalGrade <= 78:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.75. You Passed!")
    elif roundFinalGrade == 75:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 3.00. You Passed!")
    else:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 5.00. You Failed!")
def exercise_6():
    #Name: Irish B. De Guzman
    #Date: November 13, 2025
    #Title: Exercise 6 - Asterisk

    while True:
        print ("Select Pattern")
        print ("A, B, C")
        choice = input("Enter your selected pattern: ")

    # pattern A
        if choice == "A" or choice == "a":
            print ("\nA")
            a = 5
            for i in range (a):
                for A in range (i + 1):
                    print ("*", end =" ")
                print ()
            a = 4
            for i in range (a):
                for A in range (i, a):
                    print ("*", end = " ")
                print()
        
    #pattern B
        elif choice == "B" or choice == "b":
            print ("\nB")
            b = 4
            for i in range (b):
                for B in range (i, b):
                    print (" ", end = " ")
                for B in range (i+1):
                    print ("*", end = " ")
                print ()
            b = 5
            for i in range (b):
                for B in range (i):
                    print(" ", end = " ")
                for B in range (i, b):
                    print ("*", end =" ")
                print ()

    #pattern C
        elif choice == "C" or choice == "c":
            print("\nC")
            for x in range(1, 10):
                if x == 5:
                    asterisk = x - 1
                    space = 2 * (5 - x) - 1
                    print("*", end=" ")
                elif x < 5:
                    asterisk = x
                    space = 2 * (5 - asterisk) - 1
                else:
                    asterisk = 10 - x
                    space = 2 * (5 - asterisk) - 1
                for i in range(asterisk):
                    print("*", end=" ")
                for i in range(space):
                    print(" ", end=" ")
                for i in range(asterisk):
                    print("*", end=" ")
                print()
                
        while True:
            again = input("\nDo you want to select another pattern? (Y/N): ").strip().upper()

            if again == "Y":
                break
            elif again == "N":
                print("Done.")
                exit()
            else:
                print("Invalid input! Please enter Y or N only.")

while True:
    choice = input("Enter the number of exercise you want to run: ")
    try:
        choice_int = int(choice)
        if choice_int == 1:
            exercise_1()
        elif choice_int == 2:
            exercise_2()
        elif choice_int == 2:
            exercise_2()
        elif choice_int == 2:
            exercise_2()
        elif choice_int == 2:
            exercise_2()
        elif choice_int == 2:
            exercise_2()
        else:
            print("Your input is out of range. Please enter a number from 1-6.")
            continue
    except:
        print("Invalid input. You must enter a number.")
        continue

    while True:
        choice_2 = input("Do you want to run another exercise?: ").strip().upper()
        if choice_2 == "YES":
            break
        elif choice_2 == "NO":
            print("Thank you!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

















