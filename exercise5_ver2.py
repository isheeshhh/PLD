print("Grades Computation")
print("\nLecture\n")

print("\nAssignment\n")

#inputs the number of Assignment(Lecture)
lecAssList = []
lecAss = 0

while True:
    lecAssNum = input("Enter the number of Assignments: ")
    try:
        lecAssNumInput = int(lecAssNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(lecAssList) < (lecAssNumInput):
    lecAss += 1
    lecAssList.append(None)
    lecAssInput = input(f"Enter your grade in Assignment{lecAss}: ")
    
    try:
        lecAssScore = int(lecAssInput)
        lecAssList[-1] = lecAssScore

    except:
        print("Invalid input.")
        lecAssList.pop()
        lecAss -= 1
        continue

#computes the total of scores
lecAssTotal = sum(lecAssList)

#computes the percentage score
lecAssPs = (lecAssTotal / (lecAssNumInput * 100)) * 100

#computes the weighted score
lecAssWs = lecAssPs * 0.15

print("\nProject\n")

#inputs the number of Project(Lecture)
lecProjList = []
lecProj = 0

while True:
    lecProjNum = input("Enter the number of Projects: ")
    try:
        lecProjNumInput = int(lecProjNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(lecProjList) < (lecProjNumInput):
    lecProj += 1
    lecProjList.append(None)
    lecProjInput = input(f"Enter your grade in Project{lecProj}: ")
    
    try:
        lecProjScore = int(lecProjInput)
        lecProjList[-1] = lecProjScore

    except:
        print("Invalid input.")
        lecProjList.pop()
        lecProj -= 1
        continue

#computes the total of scores
lecProjTotal = sum(lecProjList)

#computes the percentage score
lecProjPs = (lecProjTotal / (lecProjNumInput * 100)) * 100

#computes the weighted score
lecProjWs = lecProjPs * 0.20

print("\nRecitation\n")

#inputs the number of Recitation(Lecture)
lecRecitList = []
lecRecit = 0

while True:
    lecRecitNum = input("Enter the number of Recitations: ")
    try:
        lecRecitNumInput = int(lecRecitNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(lecRecitList) < (lecRecitNumInput):
    lecRecit += 1
    lecRecitList.append(None)
    lecRecitInput = input(f"Enter your grade in Recitation{lecRecit}: ")
    
    try:
        lecRecitScore = int(lecRecitInput)
        lecRecitList[-1] = lecRecitScore

    except:
        print("Invalid input.")
        lecRecitList.pop()
        lecRecit -= 1
        continue

#computes the total of scores
lecRecitTotal = sum(lecRecitList)

#computes the percentage score
lecRecitPs = (lecRecitTotal / (lecRecitNumInput * 100)) * 100

#computes the weighted score
lecRecitWs = lecRecitPs * 0.10

print("\nQuiz\n")

#inputs the number of Quiz(Lecture)
lecQuizList = []
lecQuiz = 0

while True:
    lecQuizNum = input("Enter the number of Quizs: ")
    try:
        lecQuizNumInput = int(lecQuizNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(lecQuizList) < (lecQuizNumInput):
    lecQuiz += 1
    lecQuizList.append(None)
    lecQuizInput = input(f"Enter your grade in Quiz{lecQuiz}: ")
    
    try:
        lecQuizScore = int(lecQuizInput)
        lecQuizList[-1] = lecQuizScore

    except:
        print("Invalid input.")
        lecQuizList.pop()
        lecQuiz -= 1
        continue

#computes the total of scores
lecQuizTotal = sum(lecQuizList)

#computes the percentage score
lecQuizPs = (lecQuizTotal / (lecQuizNumInput * 100)) * 100

#computes the weighted score
lecQuizWs = lecQuizPs * 0.25

print("\nExamination\n")

#inputs the number of Examination(Lecture)
lecExamList = []
lecExam = 0

while True:
    lecExamNum = input("Enter the number of Examinations: ")
    try:
        lecExamNumInput = int(lecExamNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(lecExamList) < (lecExamNumInput):
    lecExam += 1
    lecExamList.append(None)
    lecExamInput = input(f"Enter your grade in Examination{lecExam}: ")
    
    try:
        lecExamScore = int(lecExamInput)
        lecExamList[-1] = lecExamScore

    except:
        print("Invalid input.")
        lecExamList.pop()
        lecExam -= 1
        continue

#computes the total of scores
lecExamTotal = sum(lecExamList)

#computes the percentage score
lecExamPs = (lecExamTotal / (lecExamNumInput * 100)) * 100

#computes the weighted score
lecExamWs = lecExamPs * 0.30

print("\nLaboratory\n")

print("\nAssignment\n")

#inputs the number of Assignment(Laboratory)
labAssList = []
labAss = 0

while True:
    labAssNum = input("Enter the number of Assignments: ")
    try:
        labAssNumInput = int(labAssNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(labAssList) < (labAssNumInput):
    labAss += 1
    labAssList.append(None)
    labAssInput = input(f"Enter your grade in Assignment{labAss}: ")
    
    try:
        labAssScore = int(labAssInput)
        labAssList[-1] = labAssScore

    except:
        print("Invalid input.")
        labAssList.pop()
        labAss -= 1
        continue

#computes the total of scores
labAssTotal = sum(labAssList)

#computes the percentage score
labAssPs = (labAssTotal / (labAssNumInput * 100)) * 100

#computes the weighted score
labAssWs = labAssPs * 0.15

print("\nProject\n")

#inputs the number of Project(Laboratory)
labProjList = []
labProj = 0

while True:
    labProjNum = input("Enter the number of Projects: ")
    try:
        labProjNumInput = int(labProjNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(labProjList) < (labProjNumInput):
    labProj += 1
    labProjList.append(None)
    labProjInput = input(f"Enter your grade in Project{labProj}: ")
    
    try:
        labProjScore = int(labProjInput)
        labProjList[-1] = labProjScore

    except:
        print("Invalid input.")
        labProjList.pop()
        labProj -= 1
        continue

#computes the total of scores
labProjTotal = sum(labProjList)

#computes the percentage score
labProjPs = (labProjTotal / (labProjNumInput * 100)) * 100

#computes the weighted score
labProjWs = labProjPs * 0.20

print("\nRecitation\n")

#inputs the number of Recitation(Laboratory)
labRecitList = []
labRecit = 0

while True:
    labRecitNum = input("Enter the number of Recitations: ")
    try:
        labRecitNumInput = int(labRecitNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(labRecitList) < (labRecitNumInput):
    labRecit += 1
    labRecitList.append(None)
    labRecitInput = input(f"Enter your grade in Recitation{labRecit}: ")
    
    try:
        labRecitScore = int(labRecitInput)
        labRecitList[-1] = labRecitScore

    except:
        print("Invalid input.")
        labRecitList.pop()
        labRecit -= 1
        continue

#computes the total of scores
labRecitTotal = sum(labRecitList)

#computes the percentage score
labRecitPs = (labRecitTotal / (labRecitNumInput * 100)) * 100

#computes the weighted score
labRecitWs = labRecitPs * 0.10

print("\nQuiz\n")

#inputs the number of Quiz(Laboratory)
labQuizList = []
labQuiz = 0

while True:
    labQuizNum = input("Enter the number of Quizs: ")
    try:
        labQuizNumInput = int(labQuizNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(labQuizList) < (labQuizNumInput):
    labQuiz += 1
    labQuizList.append(None)
    labQuizInput = input(f"Enter your grade in Quiz{labQuiz}: ")
    
    try:
        labQuizScore = int(labQuizInput)
        labQuizList[-1] = labQuizScore

    except:
        print("Invalid input.")
        labQuizList.pop()
        labQuiz -= 1
        continue

#computes the total of scores
labQuizTotal = sum(labQuizList)

#computes the percentage score
labQuizPs = (labQuizTotal / (labQuizNumInput * 100)) * 100

#computes the weighted score
labQuizWs = labQuizPs * 0.25

print("\nExamination\n")

#inputs the number of Examination(Laboratory)
labExamList = []
labExam = 0

while True:
    labExamNum = input("Enter the number of Examinations: ")
    try:
        labExamNumInput = int(labExamNum)
        break
    except:
        print("Invlid input.")
        continue

#loop that gets the scores
while len(labExamList) < (labExamNumInput):
    labExam += 1
    labExamList.append(None)
    labExamInput = input(f"Enter your grade in Examination{labExam}: ")
    
    try:
        labExamScore = int(labExamInput)
        labExamList[-1] = labExamScore

    except:
        print("Invalid input.")
        labExamList.pop()
        labExam -= 1
        continue

#computes the total of scores
labExamTotal = sum(labExamList)

#computes the percentage score
labExamPs = (labExamTotal / (labExamNumInput * 100)) * 100

#computes the weighted score
labExamWs = labExamPs * 0.30

#computes the final grade for lecture
finalLec = lecAssWs + lecProjWs + lecRecitWs + lecQuizWs + lecExamWs

#computes the final grade for laboratory
finalLab = labAssWs + labProjWs + labRecitWs + labQuizWs + labExamWs

#computes the final grade
finalGrade = (finalLec * 0.70) + (finalLab * 0.30)

#rounds off the final grade to the nearest hundreths
roundedFinalGrade = round(finalGrade, 2)

#rounds up or rounds down the final grade
integer_part = int(roundedFinalGrade)
decimal_part = round(roundedFinalGrade - integer_part, 2)

if decimal_part >= 0.45:
    roundFinalGrade = integer_part + 1
else:
    roundFinalGrade = integer_part

print("\nAssignment (Lecture)")
for index, items in enumerate(lecAssList):
    print(f"Assignment {index + 1} = {items}")
print("------------------------------------")

print("Project (Lecture)")
for index, items in enumerate(lecProjList):
    print(f"Project {index + 1} = {items}")
print("------------------------------------")

print("Recitation (Lecture)")
for index, items in enumerate(lecRecitList):
    print(f"Recitation {index + 1} = {items}")
print("------------------------------------")

print("Quiz (Lecture)")
for index, items in enumerate(lecQuizList):
    print(f"Quiz {index + 1} = {items}")
print("------------------------------------")

print("Examination (Lecture)")
for index, items in enumerate(lecExamList):
    print(f"Examination {index + 1} = {items}")
print("------------------------------------")

print("Assignment (Laboratory)")
for index, items in enumerate(labAssList):
    print(f"Assignment {index + 1} = {items}")
print("------------------------------------")

print("Project (Laboratory)")
for index, items in enumerate(labProjList):
    print(f"Project {index + 1} = {items}")
print("------------------------------------")

print("Recitation (Laboratory)")
for index, items in enumerate(labRecitList):
    print(f"Recitation {index + 1} = {items}")
print("------------------------------------")

print("Quiz (Laboratory)")
for index, items in enumerate(labQuizList):
    print(f"Quiz {index + 1} = {items}")
print("------------------------------------")

print("Examination (Laboratory)")
for index, items in enumerate(labExamList):
    print(f"Examination {index + 1} = {items}")
print("------------------------------------\n")

print("Final Lecture: ", finalLec)
print("Final Lab: ", finalLab)
print("Rounded Final Grade: ", roundFinalGrade, "\n")

#outputs the final grade and remarks
if roundFinalGrade >= 97 and roundedFinalGrade <= 100:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 1.00. You Passed!")
elif roundFinalGrade >= 94 and roundedFinalGrade <= 96:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 1.25. You Passed!")
elif roundFinalGrade >= 91 and roundedFinalGrade <= 93:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 1.50. You Passed!")
elif roundFinalGrade >= 88 and roundedFinalGrade <= 90:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 1.75. You Passed!")
elif roundedFinalGrade >= 85 and roundedFinalGrade <= 87:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 2.00. You Passed!")
elif roundFinalGrade >= 82 and roundedFinalGrade <= 84:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 2.25. You Passed!")
elif roundFinalGrade >= 79 and roundedFinalGrade <= 81:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 2.50. You Passed!")
elif roundFinalGrade >= 76 and roundedFinalGrade <= 78:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 2.75. You Passed!")
elif roundFinalGrade == 75:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 3.00. You Passed!")
else:
    print("Your final grade is", roundedFinalGrade, "which is equivalent to 5.00. You Failed!")


