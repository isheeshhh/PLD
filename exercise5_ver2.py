#Name: Irish B. De Guzman
#Date: November 15, 2025
#Title: Exercise 5 - Grades Computation

print("Grades Computation")
print("\nLecture\n")

print("Assignment\n")

#inputs the number of Assignment (Lecture)
lecAssNum = int(input("Enter the number of Assignments: "))
lecAssList = []
lecAss = 0

#loop that gets the scores
while len(lecAssList) < (lecAssNum):
    lecAss += 1
    lecAssInput = float(input(f"Enter your grade in Assignment {lecAss}: "))
    lecAssList.append(lecAssInput)

#computes the total of scores
lecAssTotal = sum(lecAssList)

#computes the percentage score
lecAssPs = (lecAssTotal / (lecAssNum * 100)) * 100

#computes the weighted score
lecAssWs = lecAssPs * 0.15

print("\nProject\n")

#inputs the number of Project (Lecture)
lecProjNum = int(input("Enter the number of Projects: "))
lecProjList = []
lecProj = 0

#loop that gets the scores
while len(lecProjList) < (lecProjNum):
    lecProj += 1
    lecProjInput = float(input(f"Enter your grade in Project {lecProj}: "))
    lecProjList.append(lecProjInput)

#computes the total of scores
lecProjTotal = sum(lecProjList)

#computes the percentage score
lecProjPs = (lecProjTotal / (lecProjNum * 100)) * 100

#computes the weighted score
lecProjWs = lecProjPs * 0.20

print("\nRecitation\n")

#inputs the number of Recitation (Lecture)
lecRecitNum = int(input("Enter the number of Recitations: "))
lecRecitList = []
lecRecit = 0

#loop that gets the scores
while len(lecRecitList) < (lecRecitNum):
    lecRecit += 1
    lecRecitInput = float(input(f"Enter your grade in Recitation {lecRecit}: "))
    lecRecitList.append(lecRecitInput)

#computes the total of scores
lecRecitTotal = sum(lecRecitList)

#computes the percentage score
lecRecitPs = (lecRecitTotal / (lecRecitNum * 100)) * 100

#computes the weighted score
lecRecitWs = lecRecitPs * 0.10

print("\nQuiz\n")

#inputs the number of Quiz (Lecture)
lecQuizNum = int(input("Enter the number of Quizzes: "))
lecQuizList = []
lecQuiz = 0

#loop that gets the scores
while len(lecQuizList) < (lecQuizNum):
    lecQuiz += 1
    lecQuizInput = float(input(f"Enter your grade in Quiz {lecQuiz}: "))
    lecQuizList.append(lecQuizInput)

#computes the total of scores
lecQuizTotal = sum(lecQuizList)

#computes the percentage score
lecQuizPs = (lecQuizTotal / (lecQuizNum * 100)) * 100

#computes the weighted score
lecQuizWs = lecQuizPs * 0.25

print("\nExamination\n")

#inputs the number of Examination (Lecture)
lecExamNum = int(input("Enter the number of Examinations: "))
lecExamList = []
lecExam = 0

#loop that gets the scores
while len(lecExamList) < (lecExamNum):
    lecExam += 1
    lecExamInput = float(input(f"Enter your grade in Examination {lecExam}: "))
    lecExamList.append(lecExamInput)

#computes the total of scores
lecExamTotal = sum(lecExamList)

#computes the percentage score
lecExamPs = (lecExamTotal / (lecExamNum * 100)) * 100

#computes the weighted score
lecExamWs = lecExamPs * 0.30

print("\nLaboratory\n")

print("Assignment\n")

#inputs the number of Assignment (Laboratory)
labAssNum = int(input("Enter the number of Assignments: "))
labAssList = []
labAss = 0

#loop that gets the scores
while len(labAssList) < (labAssNum):
    labAss += 1
    labAssInput = float(input(f"Enter your grade in Assignment {labAss}: "))
    labAssList.append(labAssInput)

#computes the total of scores
labAssTotal = sum(labAssList)

#computes the percentage score
labAssPs = (labAssTotal / (labAssNum * 100)) * 100

#computes the weighted score
labAssWs = labAssPs * 0.15

print("\nProject\n")

#inputs the number of Project (Laboratory)
labProjNum = int(input("Enter the number of Projects: "))
labProjList = []
labProj = 0

#loop that gets the scores
while len(labProjList) < (labProjNum):
    labProj += 1
    labProjInput = float(input(f"Enter your grade in Project {labProj}: "))
    labProjList.append(labProjInput)

#computes the total of scores
labProjTotal = sum(labProjList)

#computes the percentage score
labProjPs = (labProjTotal / (labProjNum * 100)) * 100

#computes the weighted score
labProjWs = labProjPs * 0.20

print("\nRecitation\n")

#inputs the number of Recitation (Laboratory)
labRecitNum = int(input("Enter the number of Recitations: "))
labRecitList = []
labRecit = 0

#loop that gets the scores
while len(labRecitList) < (labRecitNum):
    labRecit += 1
    labRecitInput = float(input(f"Enter your grade in Recitation {labRecit}: "))
    labRecitList.append(labRecitInput)

#computes the total of scores
labRecitTotal = sum(labRecitList)

#computes the percentage score
labRecitPs = (labRecitTotal / (labRecitNum * 100)) * 100

#computes the weighted score
labRecitWs = labRecitPs * 0.10

print("\nQuiz\n")

#inputs the number of Quiz (Laboratory)
labQuizNum = int(input("Enter the number of Quizzes: "))
labQuizList = []
labQuiz = 0

#loop that gets the scores
while len(labQuizList) < (labQuizNum):
    labQuiz += 1
    labQuizInput = float(input(f"Enter your grade in Quiz {labQuiz}: "))
    labQuizList.append(labQuizInput)

#computes the total of scores
labQuizTotal = sum(labQuizList)

#computes the percentage score
labQuizPs = (labQuizTotal / (labQuizNum * 100)) * 100

#computes the weighted score
labQuizWs = labQuizPs * 0.25

print("\nExamination\n")

#inputs the number of Examination (Laboratory)
labExamNum = int(input("Enter the number of Examinations: "))
labExamList = []
labExam = 0

#loop that gets the scores
while len(labExamList) < (labExamNum):
    labExam += 1
    labExamInput = float(input(f"Enter your grade in Examination {labExam}: "))
    labExamList.append(labExamInput)

#computes the total of scores
labExamTotal = sum(labExamList)

#computes the percentage score
labExamPs = (labExamTotal / (labExamNum * 100)) * 100

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
integer = int(roundedFinalGrade)
decimal = roundedFinalGrade - integer

if decimal >= 0.45:
    roundFinalGrade = integer + 1
else:
    roundFinalGrade = integer

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
elif roundFinalGrade >= 85 and roundedFinalGrade <= 87:
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

