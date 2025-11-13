#Name: Irish B. De Guzman
#Date: November 13, 2025
#Title: Exercise 5 - Grades Computation

print("Grade Computation")
print("\nLecture\n")

print("Assignment\n")

#initialize the value
lecAssTotal = 0
lecAssPerfectScoreTotal = 0
lecAssList = []
lecAssPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Assignment (lecture)
while True:
    lecAssInput = input("Enter your score: ").upper()
    lecAssPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if lecAssInput == '-' and lecAssPerfectScoreInput == '-':
        break
    
    #append scores first
    if lecAssInput != "REPLACE":
        try:
            lecAss = float(lecAssInput)
            lecAssList.append(lecAss) 
        except:
            if lecAssInput != '-':
                print("Invalid input for score.")
    
    if lecAssPerfectScoreInput != "REPLACE":
        try:
            lecAssPerfectScore = float(lecAssPerfectScoreInput)
            lecAssPerfectScoreList.append(lecAssPerfectScore)
        except:
            if lecAssPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if lecAssInput == "REPLACE" or lecAssPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Assignment number you want to replace
                while True: 
                    lecAssScoreIndexInput = input("Enter the Assignment number you want to replace: ")

                    if not lecAssScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Assignment number you want to replace. ")
                        continue
                    else:
                        lecAssScoreIndex = int(lecAssScoreIndexInput) - 1
                    
                    if 0 <= lecAssScoreIndex < len(lecAssList):
                        break
                    else:
                        print("Assignment number is out of range. Please enter a valid Assignment number.")
                        continue

                #inputs the new value
                while True:
                    lecAssNewValueInput = input("Enter the new score value: ")

                    try:
                        lecAssNewValue = float(lecAssNewValueInput)
                        lecAssList[lecAssScoreIndex] = lecAssNewValue
                        print(f"Updated score: Assignment {lecAssScoreIndex + 1}: {lecAssNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Assignment number you want to replace
                while True: 
                    lecAssPerfectScoreIndexInput = input("Enter the Assignment number you want to replace: ")

                    if not lecAssPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Assignment number you want to replace. ")
                        continue
                    else:
                        lecAssPerfectScoreIndex = int(lecAssPerfectScoreIndexInput) - 1
                    
                    if 0 <= lecAssPerfectScoreIndex < len(lecAssPerfectScoreList):
                        break
                    else:
                        print("Assignment number is out of range. Please enter a valid Assignment number.")
                        continue
                
                #inputs the new value
                while True:
                    lecAssPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        lecAssPerfectScoreNewValue = float(lecAssPerfectScoreNewValueInput)
                        lecAssPerfectScoreList[lecAssPerfectScoreIndex] = lecAssPerfectScoreNewValue
                        print(f"Updated perfect score: Assignment {lecAssPerfectScoreIndex + 1}: {lecAssPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
lecAssTotal = sum(lecAssList)

#computes the sum of perfect scores
lecAssPerfectScoreTotal = sum(lecAssPerfectScoreList)

#computes the percentage score and weighted score
if lecAssPerfectScoreTotal > 0:
    lecAssPs = ((lecAssTotal / lecAssPerfectScoreTotal) * 100)
    lecAssWs = lecAssPs * 0.15
else:
    lecAssPs = 0
    lecAssWs = 0

print("\nProject\n")

#initialize the value
lecProjTotal = 0
lecProjPerfectScoreTotal = 0
lecProjList = []
lecProjPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Project (lecture)
while True:
    lecProjInput = input("Enter your score: ").upper()
    lecProjPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if lecProjInput == '-' and lecProjPerfectScoreInput == '-':
        break
    
    #append scores first
    if lecProjInput != "REPLACE":
        try:
            lecProj = float(lecProjInput)
            lecProjList.append(lecProj) 
        except:
            if lecProjInput != '-':
                print("Invalid input for score.")
    
    if lecProjPerfectScoreInput != "REPLACE":
        try:
            lecProjPerfectScore = float(lecProjPerfectScoreInput)
            lecProjPerfectScoreList.append(lecProjPerfectScore)
        except:
            if lecProjPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if lecProjInput == "REPLACE" or lecProjPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Project number you want to replace
                while True: 
                    lecProjScoreIndexInput = input("Enter the Project number you want to replace: ")

                    if not lecProjScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Project number you want to replace. ")
                        continue
                    else:
                        lecProjScoreIndex = int(lecProjScoreIndexInput) - 1
                    
                    if 0 <= lecProjScoreIndex < len(lecProjList):
                        break
                    else:
                        print("Project number is out of range. Please enter a valid Project number.")
                        continue

                #inputs the new value
                while True:
                    lecProjNewValueInput = input("Enter the new score value: ")

                    try:
                        lecProjNewValue = float(lecProjNewValueInput)
                        lecProjList[lecProjScoreIndex] = lecProjNewValue
                        print(f"Updated score: Project {lecProjScoreIndex + 1}: {lecProjNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Project number you want to replace
                while True: 
                    lecProjPerfectScoreIndexInput = input("Enter the Project number you want to replace: ")

                    if not lecProjPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Project number you want to replace. ")
                        continue
                    else:
                        lecProjPerfectScoreIndex = int(lecProjPerfectScoreIndexInput) - 1
                    
                    if 0 <= lecProjPerfectScoreIndex < len(lecProjPerfectScoreList):
                        break
                    else:
                        print("Project number is out of range. Please enter a valid Project number.")
                        continue
                
                #inputs the new value
                while True:
                    lecProjPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        lecProjPerfectScoreNewValue = float(lecProjPerfectScoreNewValueInput)
                        lecProjPerfectScoreList[lecProjPerfectScoreIndex] = lecProjPerfectScoreNewValue
                        print(f"Updated perfect score: Project {lecProjPerfectScoreIndex + 1}: {lecProjPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
lecProjTotal = sum(lecProjList)

#computes the sum of perfect scores
lecProjPerfectScoreTotal = sum(lecProjPerfectScoreList)

#computes the percentage score and weighted score
if lecProjPerfectScoreTotal > 0:
    lecProjPs = ((lecProjTotal / lecProjPerfectScoreTotal) * 100)
    lecProjWs = lecProjPs * 0.20
else:
    lecProjPs = 0
    lecProjWs = 0

print("\nRecitation\n")

#initialize the value
lecRecitTotal = 0
lecRecitPerfectScoreTotal = 0
lecRecitList = []
lecRecitPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Recitation (lecture)
while True:
    lecRecitInput = input("Enter your score: ").upper()
    lecRecitPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if lecRecitInput == '-' and lecRecitPerfectScoreInput == '-':
        break
    
    #append scores first
    if lecRecitInput != "REPLACE":
        try:
            lecRecit = float(lecRecitInput)
            lecRecitList.append(lecRecit) 
        except:
            if lecRecitInput != '-':
                print("Invalid input for score.")
    
    if lecRecitPerfectScoreInput != "REPLACE":
        try:
            lecRecitPerfectScore = float(lecRecitPerfectScoreInput)
            lecRecitPerfectScoreList.append(lecRecitPerfectScore)
        except:
            if lecRecitPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if lecRecitInput == "REPLACE" or lecRecitPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Recitation number you want to replace
                while True: 
                    lecRecitScoreIndexInput = input("Enter the Recitation number you want to replace: ")

                    if not lecRecitScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Recitation number you want to replace. ")
                        continue
                    else:
                        lecRecitScoreIndex = int(lecRecitScoreIndexInput) - 1
                    
                    if 0 <= lecRecitScoreIndex < len(lecRecitList):
                        break
                    else:
                        print("Recitation number is out of range. Please enter a valid Recitation number.")
                        continue

                #inputs the new value
                while True:
                    lecRecitNewValueInput = input("Enter the new score value: ")

                    try:
                        lecRecitNewValue = float(lecRecitNewValueInput)
                        lecRecitList[lecRecitScoreIndex] = lecRecitNewValue
                        print(f"Updated score: Recitation {lecRecitScoreIndex + 1}: {lecRecitNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Recitation number you want to replace
                while True: 
                    lecRecitPerfectScoreIndexInput = input("Enter the Recitation number you want to replace: ")

                    if not lecRecitPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Recitation number you want to replace. ")
                        continue
                    else:
                        lecRecitPerfectScoreIndex = int(lecRecitPerfectScoreIndexInput) - 1
                    
                    if 0 <= lecRecitPerfectScoreIndex < len(lecRecitPerfectScoreList):
                        break
                    else:
                        print("Recitation number is out of range. Please enter a valid Recitation number.")
                        continue
                
                #inputs the new value
                while True:
                    lecRecitPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        lecRecitPerfectScoreNewValue = float(lecRecitPerfectScoreNewValueInput)
                        lecRecitPerfectScoreList[lecRecitPerfectScoreIndex] = lecRecitPerfectScoreNewValue
                        print(f"Updated perfect score: Recitation {lecRecitPerfectScoreIndex + 1}: {lecRecitPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
lecRecitTotal = sum(lecRecitList)

#computes the sum of perfect scores
lecRecitPerfectScoreTotal = sum(lecRecitPerfectScoreList)

#computes the percentage score and weighted score
if lecRecitPerfectScoreTotal > 0:
    lecRecitPs = ((lecRecitTotal / lecRecitPerfectScoreTotal) * 100)
    lecRecitWs = lecRecitPs * 0.10
else:
    lecRecitPs = 0
    lecRecitWs = 0

print("\nQuiz\n")

#initialize the value
lecQuizTotal = 0
lecQuizPerfectScoreTotal = 0
lecQuizList = []
lecQuizPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Quiz (lecture)
while True:
    lecQuizInput = input("Enter your score: ").upper()
    lecQuizPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if lecQuizInput == '-' and lecQuizPerfectScoreInput == '-':
        break
    
    #append scores first
    if lecQuizInput != "REPLACE":
        try:
            lecQuiz = float(lecQuizInput)
            lecQuizList.append(lecQuiz) 
        except:
            if lecQuizInput != '-':
                print("Invalid input for score.")
    
    if lecQuizPerfectScoreInput != "REPLACE":
        try:
            lecQuizPerfectScore = float(lecQuizPerfectScoreInput)
            lecQuizPerfectScoreList.append(lecQuizPerfectScore)
        except:
            if lecQuizPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if lecQuizInput == "REPLACE" or lecQuizPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Quiz number you want to replace
                while True: 
                    lecQuizScoreIndexInput = input("Enter the Quiz number you want to replace: ")

                    if not lecQuizScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Quiz number you want to replace. ")
                        continue
                    else:
                        lecQuizScoreIndex = int(lecQuizScoreIndexInput) - 1
                    
                    if 0 <= lecQuizScoreIndex < len(lecQuizList):
                        break
                    else:
                        print("Quiz number is out of range. Please enter a valid Quiz number.")
                        continue

                #inputs the new value
                while True:
                    lecQuizNewValueInput = input("Enter the new score value: ")

                    try:
                        lecQuizNewValue = float(lecQuizNewValueInput)
                        lecQuizList[lecQuizScoreIndex] = lecQuizNewValue
                        print(f"Updated score: Quiz {lecQuizScoreIndex + 1}: {lecQuizNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Quiz number you want to replace
                while True: 
                    lecQuizPerfectScoreIndexInput = input("Enter the Quiz number you want to replace: ")

                    if not lecQuizPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Quiz number you want to replace. ")
                        continue
                    else:
                        lecQuizPerfectScoreIndex = int(lecQuizPerfectScoreIndexInput) - 1
                    
                    if 0 <= lecQuizPerfectScoreIndex < len(lecQuizPerfectScoreList):
                        break
                    else:
                        print("Quiz number is out of range. Please enter a valid Quiz number.")
                        continue

                #inputs the new value
                while True:
                    lecQuizPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        lecQuizPerfectScoreNewValue = float(lecQuizPerfectScoreNewValueInput)
                        lecQuizPerfectScoreList[lecQuizPerfectScoreIndex] = lecQuizPerfectScoreNewValue
                        print(f"Updated perfect score: Quiz {lecQuizPerfectScoreIndex + 1}: {lecQuizPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
lecQuizTotal = sum(lecQuizList)

#computes the sum of perfect scores
lecQuizPerfectScoreTotal = sum(lecQuizPerfectScoreList)

#computes the percentage score and weighted score
if lecQuizPerfectScoreTotal > 0:
    lecQuizPs = ((lecQuizTotal / lecQuizPerfectScoreTotal) * 100)
    lecQuizWs = lecQuizPs * 0.25
else:
    lecQuizPs = 0
    lecQuizWs = 0

print("\nExamination\n")

#initialize the value
lecExamTotal = 0
lecExamPerfectScoreTotal = 0
lecExamList = []
lecExamPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Examination (lecture)
while True:
    lecExamInput = input("Enter your score: ").upper()
    lecExamPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if lecExamInput == '-' and lecExamPerfectScoreInput == '-':
        break
    
    #append scores first
    if lecExamInput != "REPLACE":
        try:
            lecExam = float(lecExamInput)
            lecExamList.append(lecExam) 
        except:
            if lecExamInput != '-':
                print("Invalid input for score.")
    
    if lecExamPerfectScoreInput != "REPLACE":
        try:
            lecExamPerfectScore = float(lecExamPerfectScoreInput)
            lecExamPerfectScoreList.append(lecExamPerfectScore)
        except:
            if lecExamPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if lecExamInput == "REPLACE" or lecExamPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Examination number you want to replace
                while True: 
                    lecExamScoreIndexInput = input("Enter the Examination number you want to replace: ")

                    if not lecExamScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Examination number you want to replace. ")
                        continue
                    else:
                        lecExamScoreIndex = int(lecExamScoreIndexInput) - 1
                    
                    if 0 <= lecExamScoreIndex < len(lecExamList):
                        break
                    else:
                        print("Examination number is out of range. Please enter a valid Examination number.")
                        continue

                #inputs the new value
                while True:
                    lecExamNewValueInput = input("Enter the new score value: ")

                    try:
                        lecExamNewValue = float(lecExamNewValueInput)
                        lecExamList[lecExamScoreIndex] = lecExamNewValue
                        print(f"Updated score: Examination {lecExamScoreIndex + 1}: {lecExamNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Examination number you want to replace
                while True: 
                    lecExamPerfectScoreIndexInput = input("Enter the Examination number you want to replace: ")

                    if not lecExamPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Examination number you want to replace. ")
                        continue
                    else:
                        lecExamPerfectScoreIndex = int(lecExamPerfectScoreIndexInput) - 1
                    
                    if 0 <= lecExamPerfectScoreIndex < len(lecExamPerfectScoreList):
                        break
                    else:
                        print("Examination number is out of range. Please enter a valid Examination number.")
                        continue
                
                #inputs the new value
                while True:
                    lecExamPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        lecExamPerfectScoreNewValue = float(lecExamPerfectScoreNewValueInput)
                        lecExamPerfectScoreList[lecExamPerfectScoreIndex] = lecExamPerfectScoreNewValue
                        print(f"Updated perfect score: Examination {lecExamPerfectScoreIndex + 1}: {lecExamPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
lecExamTotal = sum(lecExamList)

#computes the sum of perfect scores
lecExamPerfectScoreTotal = sum(lecExamPerfectScoreList)

#computes the percentage score and weighted score
if lecExamPerfectScoreTotal > 0:
    lecExamPs = ((lecExamTotal / lecExamPerfectScoreTotal) * 100)
    lecExamWs = lecExamPs * 0.30
else:
    lecExamPs = 0
    lecExamWs = 0

print("\nAssignment\n")

#initialize the value
labAssTotal = 0
labAssPerfectScoreTotal = 0
labAssList = []
labAssPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Assignment (laboratory)
while True:
    labAssInput = input("Enter your score: ").upper()
    labAssPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if labAssInput == '-' and labAssPerfectScoreInput == '-':
        break
    
    #append scores first
    if labAssInput != "REPLACE":
        try:
            labAss = float(labAssInput)
            labAssList.append(labAss) 
        except:
            if labAssInput != '-':
                print("Invalid input for score.")
    
    if labAssPerfectScoreInput != "REPLACE":
        try:
            labAssPerfectScore = float(labAssPerfectScoreInput)
            labAssPerfectScoreList.append(labAssPerfectScore)
        except:
            if labAssPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if labAssInput == "REPLACE" or labAssPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Assignment number you want to replace
                while True: 
                    labAssScoreIndexInput = input("Enter the Assignment number you want to replace: ")

                    if not labAssScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Assignment number you want to replace. ")
                        continue
                    else:
                        labAssScoreIndex = int(labAssScoreIndexInput) - 1
                    
                    if 0 <= labAssScoreIndex < len(labAssList):
                        break
                    else:
                        print("Assignment number is out of range. Please enter a valid Assignment number.")
                        continue

                #inputs the new value
                while True:
                    labAssNewValueInput = input("Enter the new score value: ")

                    try:
                        labAssNewValue = float(labAssNewValueInput)
                        labAssList[labAssScoreIndex] = labAssNewValue
                        print(f"Updated score: Assignment {labAssScoreIndex + 1}: {labAssNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Assignment number you want to replace
                while True: 
                    labAssPerfectScoreIndexInput = input("Enter the Assignment number you want to replace: ")

                    if not labAssPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Assignment number you want to replace. ")
                        continue
                    else:
                        labAssPerfectScoreIndex = int(labAssPerfectScoreIndexInput) - 1
                    
                    if 0 <= labAssPerfectScoreIndex < len(labAssPerfectScoreList):
                        break
                    else:
                        print("Assignment number is out of range. Please enter a valid Assignment number.")
                        continue
                
                #inputs the new value
                while True:
                    labAssPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        labAssPerfectScoreNewValue = float(labAssPerfectScoreNewValueInput)
                        labAssPerfectScoreList[labAssPerfectScoreIndex] = labAssPerfectScoreNewValue
                        print(f"Updated perfect score: Assignment {labAssPerfectScoreIndex + 1}: {labAssPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
labAssTotal = sum(labAssList)

#computes the sum of perfect scores
labAssPerfectScoreTotal = sum(labAssPerfectScoreList)

#computes the percentage score and weighted score
if labAssPerfectScoreTotal > 0:
    labAssPs = ((labAssTotal / labAssPerfectScoreTotal) * 100)
    labAssWs = labAssPs * 0.15
else:
    labAssPs = 0
    labAssWs = 0

print("\nProject\n")

#initialize the value
labProjTotal = 0
labProjPerfectScoreTotal = 0
labProjList = []
labProjPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Project (laboratory)
while True:
    labProjInput = input("Enter your score: ").upper()
    labProjPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if labProjInput == '-' and labProjPerfectScoreInput == '-':
        break
    
    #append scores first
    if labProjInput != "REPLACE":
        try:
            labProj = float(labProjInput)
            labProjList.append(labProj) 
        except:
            if labProjInput != '-':
                print("Invalid input for score.")
    
    if labProjPerfectScoreInput != "REPLACE":
        try:
            labProjPerfectScore = float(labProjPerfectScoreInput)
            labProjPerfectScoreList.append(labProjPerfectScore)
        except:
            if labProjPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if labProjInput == "REPLACE" or labProjPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Project number you want to replace
                while True: 
                    labProjScoreIndexInput = input("Enter the Project number you want to replace: ")

                    if not labProjScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Project number you want to replace. ")
                        continue
                    else:
                        labProjScoreIndex = int(labProjScoreIndexInput) - 1
                    
                    if 0 <= labProjScoreIndex < len(labProjList):
                        break
                    else:
                        print("Project number is out of range. Please enter a valid Project number.")
                        continue

                #inputs the new value
                while True:
                    labProjNewValueInput = input("Enter the new score value: ")

                    try:
                        labProjNewValue = float(labProjNewValueInput)
                        labProjList[labProjScoreIndex] = labProjNewValue
                        print(f"Updated score: Project {labProjScoreIndex + 1}: {labProjNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Project number you want to replace
                while True: 
                    labProjPerfectScoreIndexInput = input("Enter the Project number you want to replace: ")

                    if not labProjPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Project number you want to replace. ")
                        continue
                    else:
                        labProjPerfectScoreIndex = int(labProjPerfectScoreIndexInput) - 1
                    
                    if 0 <= labProjPerfectScoreIndex < len(labProjPerfectScoreList):
                        break
                    else:
                        print("Project number is out of range. Please enter a valid Project number.")
                        continue
                
                #inputs the new value
                while True:
                    labProjPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        labProjPerfectScoreNewValue = float(labProjPerfectScoreNewValueInput)
                        labProjPerfectScoreList[labProjPerfectScoreIndex] = labProjPerfectScoreNewValue
                        print(f"Updated perfect score: Project {labProjPerfectScoreIndex + 1}: {labProjPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
labProjTotal = sum(labProjList)

#computes the sum of perfect scores
labProjPerfectScoreTotal = sum(labProjPerfectScoreList)

#computes the percentage score and weighted score
if labProjPerfectScoreTotal > 0:
    labProjPs = ((labProjTotal / labProjPerfectScoreTotal) * 100)
    labProjWs = labProjPs * 0.20
else:
    labProjPs = 0
    labProjWs = 0

print("\nRecitation\n")

#initialize the value
labRecitTotal = 0
labRecitPerfectScoreTotal = 0
labRecitList = []
labRecitPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Recitation (laboratory)
while True:
    labRecitInput = input("Enter your score: ").upper()
    labRecitPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if labRecitInput == '-' and labRecitPerfectScoreInput == '-':
        break
    
    #append scores first
    if labRecitInput != "REPLACE":
        try:
            labRecit = float(labRecitInput)
            labRecitList.append(labRecit) 
        except:
            if labRecitInput != '-':
                print("Invalid input for score.")
    
    if labRecitPerfectScoreInput != "REPLACE":
        try:
            labRecitPerfectScore = float(labRecitPerfectScoreInput)
            labRecitPerfectScoreList.append(labRecitPerfectScore)
        except:
            if labRecitPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if labRecitInput == "REPLACE" or labRecitPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Recitation number you want to replace
                while True: 
                    labRecitScoreIndexInput = input("Enter the Recitation number you want to replace: ")

                    if not labRecitScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Recitation number you want to replace. ")
                        continue
                    else:
                        labRecitScoreIndex = int(labRecitScoreIndexInput) - 1
                    
                    if 0 <= labRecitScoreIndex < len(labRecitList):
                        break
                    else:
                        print("Recitation number is out of range. Please enter a valid Recitation number.")
                        continue

                #inputs the new value
                while True:
                    labRecitNewValueInput = input("Enter the new score value: ")

                    try:
                        labRecitNewValue = float(labRecitNewValueInput)
                        labRecitList[labRecitScoreIndex] = labRecitNewValue
                        print(f"Updated score: Recitation {labRecitScoreIndex + 1}: {labRecitNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Recitation number you want to replace
                while True: 
                    labRecitPerfectScoreIndexInput = input("Enter the Recitation number you want to replace: ")

                    if not labRecitPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Recitation number you want to replace. ")
                        continue
                    else:
                        labRecitPerfectScoreIndex = int(labRecitPerfectScoreIndexInput) - 1
                    
                    if 0 <= labRecitPerfectScoreIndex < len(labRecitPerfectScoreList):
                        break
                    else:
                        print("Recitation number is out of range. Please enter a valid Recitation number.")
                        continue
                
                #inputs the new value
                while True:
                    labRecitPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        labRecitPerfectScoreNewValue = float(labRecitPerfectScoreNewValueInput)
                        labRecitPerfectScoreList[labRecitPerfectScoreIndex] = labRecitPerfectScoreNewValue
                        print(f"Updated perfect score: Recitation {labRecitPerfectScoreIndex + 1}: {labRecitPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
labRecitTotal = sum(labRecitList)

#computes the sum of perfect scores
labRecitPerfectScoreTotal = sum(labRecitPerfectScoreList)

#computes the percentage score and weighted score
if labRecitPerfectScoreTotal > 0:
    labRecitPs = ((labRecitTotal / labRecitPerfectScoreTotal) * 100)
    labRecitWs = labRecitPs * 0.10
else:
    labRecitPs = 0
    labRecitWs = 0

print("\nQuiz\n")

#initialize the value
labQuizTotal = 0
labQuizPerfectScoreTotal = 0
labQuizList = []
labQuizPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Quiz (laboratory)
while True:
    labQuizInput = input("Enter your score: ").upper()
    labQuizPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if labQuizInput == '-' and labQuizPerfectScoreInput == '-':
        break
    
    #append scores first
    if labQuizInput != "REPLACE":
        try:
            labQuiz = float(labQuizInput)
            labQuizList.append(labQuiz) 
        except:
            if labQuizInput != '-':
                print("Invalid input for score.")
    
    if labQuizPerfectScoreInput != "REPLACE":
        try:
            labQuizPerfectScore = float(labQuizPerfectScoreInput)
            labQuizPerfectScoreList.append(labQuizPerfectScore)
        except:
            if labQuizPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if labQuizInput == "REPLACE" or labQuizPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Quiz number you want to replace
                while True: 
                    labQuizScoreIndexInput = input("Enter the Quiz number you want to replace: ")

                    if not labQuizScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Quiz number you want to replace. ")
                        continue
                    else:
                        labQuizScoreIndex = int(labQuizScoreIndexInput) - 1
                    
                    if 0 <= labQuizScoreIndex < len(labQuizList):
                        break
                    else:
                        print("Quiz number is out of range. Please enter a valid Quiz number.")
                        continue

                #inputs the new value
                while True:
                    labQuizNewValueInput = input("Enter the new score value: ")

                    try:
                        labQuizNewValue = float(labQuizNewValueInput)
                        labQuizList[labQuizScoreIndex] = labQuizNewValue
                        print(f"Updated score: Quiz {labQuizScoreIndex + 1}: {labQuizNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Quiz number you want to replace
                while True: 
                    labQuizPerfectScoreIndexInput = input("Enter the Quiz number you want to replace: ")

                    if not labQuizPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Quiz number you want to replace. ")
                        continue
                    else:
                        labQuizPerfectScoreIndex = int(labQuizPerfectScoreIndexInput) - 1
                    
                    if 0 <= labQuizPerfectScoreIndex < len(labQuizPerfectScoreList):
                        break
                    else:
                        print("Quiz number is out of range. Please enter a valid Quiz number.")
                        continue
                
                #inputs the new value
                while True:
                    labQuizPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        labQuizPerfectScoreNewValue = float(labQuizPerfectScoreNewValueInput)
                        labQuizPerfectScoreList[labQuizPerfectScoreIndex] = labQuizPerfectScoreNewValue
                        print(f"Updated perfect score: Quiz {labQuizPerfectScoreIndex + 1}: {labQuizPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
labQuizTotal = sum(labQuizList)

#computes the sum of perfect scores
labQuizPerfectScoreTotal = sum(labQuizPerfectScoreList)

#computes the percentage score and weighted score
if labQuizPerfectScoreTotal > 0:
    labQuizPs = ((labQuizTotal / labQuizPerfectScoreTotal) * 100)
    labQuizWs = labQuizPs * 0.25
else:
    labQuizPs = 0
    labQuizWs = 0

print("\nExamination\n")

#initialize the value
labExamTotal = 0
labExamPerfectScoreTotal = 0
labExamList = []
labExamPerfectScoreList = []

print("Enter your score and the perfect score. If you want replace a value, type 'replace'. If you do not have inputs anymore, type '-'")

#while loop that gets the score and perfect scores for Examination (laboratory)
while True:
    labExamInput = input("Enter your score: ").upper()
    labExamPerfectScoreInput = input("Enter the perfect score: ").upper()

    #stops the loop
    if labExamInput == '-' and labExamPerfectScoreInput == '-':
        break
    
    #append scores first
    if labExamInput != "REPLACE":
        try:
            labExam = float(labExamInput)
            labExamList.append(labExam) 
        except:
            if labExamInput != '-':
                print("Invalid input for score.")
    
    if labExamPerfectScoreInput != "REPLACE":
        try:
            labExamPerfectScore = float(labExamPerfectScoreInput)
            labExamPerfectScoreList.append(labExamPerfectScore)
        except:
            if labExamPerfectScoreInput != '-':
                print("Invalid input for perfect score.")
    
    #replace the values
    if labExamInput == "REPLACE" or labExamPerfectScoreInput == "REPLACE":
        while True:
            replaceWhat = input("What do you want to replace, Score or Perfect Score?: ").upper()
            
            #replace the score
            if replaceWhat == "SCORE":
                
                #inputs the Examination number you want to replace
                while True: 
                    labExamScoreIndexInput = input("Enter the Examination number you want to replace: ")

                    if not labExamScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Examination number you want to replace. ")
                        continue
                    else:
                        labExamScoreIndex = int(labExamScoreIndexInput) - 1
                    
                    if 0 <= labExamScoreIndex < len(labExamList):
                        break
                    else:
                        print("Examination number is out of range. Please enter a valid Examination number.")
                        continue

                #inputs the new value
                while True:
                    labExamNewValueInput = input("Enter the new score value: ")

                    try:
                        labExamNewValue = float(labExamNewValueInput)
                        labExamList[labExamScoreIndex] = labExamNewValue
                        print(f"Updated score: Examination {labExamScoreIndex + 1}: {labExamNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break
            #replace the perfect score
            elif replaceWhat == "PERFECT SCORE":

                #inputs the Examination number you want to replace
                while True: 
                    labExamPerfectScoreIndexInput = input("Enter the Examination number you want to replace: ")

                    if not labExamPerfectScoreIndexInput.isdigit():
                        print("Invalid input. Please enter the Examination number you want to replace. ")
                        continue
                    else:
                        labExamPerfectScoreIndex = int(labExamPerfectScoreIndexInput) - 1
                    
                    if 0 <= labExamPerfectScoreIndex < len(labExamPerfectScoreList):
                        break
                    else:
                        print("Examination number is out of range. Please enter a valid Examination number.")
                        continue
                
                #inputs the new value
                while True:
                    labExamPerfectScoreNewValueInput = input("Enter the new perfect score value: ")

                    try:
                        labExamPerfectScoreNewValue = float(labExamPerfectScoreNewValueInput)
                        labExamPerfectScoreList[labExamPerfectScoreIndex] = labExamPerfectScoreNewValue
                        print(f"Updated perfect score: Examination {labExamPerfectScoreIndex + 1}: {labExamPerfectScoreNewValue}")
                        break
                    except:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                
                break

            else:
                print("Invalid input. Please enter Score or Perfect Score.")
                continue
        
        continue  
            
#computes the sum of scores
labExamTotal = sum(labExamList)

#computes the sum of perfect scores
labExamPerfectScoreTotal = sum(labExamPerfectScoreList)

#computes the percentage score and weighted score
if labExamPerfectScoreTotal > 0:
    labExamPs = ((labExamTotal / labExamPerfectScoreTotal) * 100)
    labExamWs = labExamPs * 0.30
else:
    labExamPs = 0
    labExamWs = 0


#for loop that outputs the scores and perfect scores
print("\nAssignment (Lecture)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(lecAssList, lecAssPerfectScoreList)):
    print(f"Assignment {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Project (Lecture)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(lecProjList, lecProjPerfectScoreList)):
    print(f"Project {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Recitation (Lecture)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(lecRecitList, lecRecitPerfectScoreList)):
    print(f"Recitation {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Quiz (Lecture)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(lecQuizList, lecQuizPerfectScoreList)):
    print(f"Quiz {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Exam (Lecture)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(lecExamList, lecExamPerfectScoreList)):
    print(f"Examination {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Assignment (Laboratory)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(labAssList, labAssPerfectScoreList)):
    print(f"Assignment {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Project (Laboratory)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(labProjList, labProjPerfectScoreList)):
    print(f"Project {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Recitation (Laboratory)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(labRecitList, labRecitPerfectScoreList)):
    print(f"Recitation {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Quiz (Laboratory)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(labQuizList, labQuizPerfectScoreList)):
    print(f"Quiz {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------")

print("Exam (Laboratory)")
for index, (itemScore, itemPerfectScore) in enumerate(zip(labExamList, labExamPerfectScoreList)):
    print(f"Examination {index + 1} = {itemScore}/{itemPerfectScore}")
print("------------------------------------\n")

#computes the total weighted scores in lecture
lecTotal = lecAssWs + lecProjWs + lecRecitWs + lecQuizWs + lecExamWs

#computes the total weighted scores in lecture
labTotal = labAssWs + labProjWs + labRecitWs + labQuizWs + labExamWs

#computes the final grade for lecture
lecFinalGrade = lecTotal * 0.70

#computes the final grade for lab
labFinalGrade = labTotal * 0.30

#computes the final grade
finalGrade = lecFinalGrade + labFinalGrade

#rounds off the final grade to the nearest hundreths
roundedFinalGrade = round(finalGrade, 2)

#rounds up or down the  rounded final grade
roundFinalGrade = int(roundedFinalGrade + 0.5)

print(f"Lecture Total: {lecTotal}")
print(f"Laboratory Total: {labTotal}")
print(f"Lecture Final Grade: {lecFinalGrade}")
print(f"Laboratory Final Grade: {labFinalGrade}")
print(f"Final Grade: {finalGrade}")
print(f"Round Final Grade: {roundFinalGrade}")

#outputs the final grade and remarks
if roundFinalGrade >= 97 and roundFinalGrade <= 100:
    print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.00. You Passed!")
elif roundFinalGrade >= 94 and roundFinalGrade <= 96:
    print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.25. You Passed!")
elif roundFinalGrade >= 91 and roundFinalGrade <= 93:
    print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.50. You Passed!")
elif roundFinalGrade >= 88 and roundFinalGrade <= 90:
    print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.75. You Passed!")
elif roundedFinalGrade >= 85 and roundFinalGrade <= 87:
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

