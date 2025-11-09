print("Grades Computation")
print("\nLecture\n")

#while loop that gets the score for assignment (lecture)
print("\nAssignement\n")
lecAssList = []
lecAssPerfectScoreList = []
lecAssTotal = 0
lecAssPerfectScoreTotal = 0
lecAss = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
lecAssPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while lecAss >= 0 and lecAssPerfectScore >= 0:
    lecAssList.append(lecAss)
    lecAssPerfectScoreList.append(lecAssPerfectScore)
    lecAssTotal += lecAss
    lecAssPerfectScoreTotal += lecAssPerfectScore
    lecAss = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    lecAssPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
lecAssPs = ((lecAssTotal / lecAssPerfectScoreTotal) * 100)
lecAssWs = lecAssPs * 0.15

#while loop that gets the score for project (lecture)
print("\nProject\n")
lecProjList = []
lecProjPerfectScoreList = []
lecProjTotal = 0
lecProjPerfectScoreTotal = 0
lecProj = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
lecProjPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while lecProj >= 0 and lecProjPerfectScore >= 0:
    lecProjList.append(lecProj)
    lecProjPerfectScoreList.append(lecProjPerfectScore)
    lecProjTotal += lecProj
    lecProjPerfectScoreTotal += lecProjPerfectScore
    lecProj = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    lecProjPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
lecProjPs = ((lecProjTotal / lecProjPerfectScoreTotal) * 100)
lecProjWs = lecProjPs * 0.20

#while loop that gets the score for recitation (lecture)
print("\nRecitation\n")
lecRecitList = []
lecRecitPerfectScoreList = []
lecRecitTotal = 0
lecRecitPerfectScoreTotal = 0
lecRecit = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
lecRecitPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while lecRecit >= 0 and lecRecitPerfectScore >= 0:
    lecRecitList.append(lecRecit)
    lecRecitPerfectScoreList.append(lecRecitPerfectScore)
    lecRecitTotal += lecRecit
    lecRecitPerfectScoreTotal += lecRecitPerfectScore
    lecRecit = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    lecRecitPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
lecRecitPs = ((lecRecitTotal / lecRecitPerfectScoreTotal) * 100)
lecRecitWs = lecRecitPs * 0.10

#while loop that gets the score for quiz (lecture)
print("\nQuiz\n")
lecQuizList = []
lecQuizPerfectScoreList = []
lecQuizTotal = 0
lecQuizPerfectScoreTotal = 0
lecQuiz = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
lecQuizPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while lecQuiz >= 0 and lecQuizPerfectScore >= 0:
    lecQuizList.append(lecQuiz)
    lecQuizPerfectScoreList.append(lecQuizPerfectScore)
    lecQuizTotal += lecQuiz
    lecQuizPerfectScoreTotal += lecQuizPerfectScore
    lecQuiz = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    lecQuizPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
lecQuizPs = ((lecQuizTotal / lecQuizPerfectScoreTotal) * 100)
lecQuizWs = lecQuizPs * 0.25

#while loop that gets the score for examination (lecture)
print("\nExamination\n")
lecExamList = []
lecExamPerfectScoreList = []
lecExamTotal = 0
lecExamPerfectScoreTotal = 0
lecExam = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
lecExamPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while lecExam >= 0 and lecExamPerfectScore >= 0:
    lecExamList.append(lecExam)
    lecExamPerfectScoreList.append(lecExamPerfectScore)
    lecExamTotal += lecExam
    lecExamPerfectScoreTotal += lecExamPerfectScore
    lecExam = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    lecExamPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
lecExamPs = ((lecExamTotal / lecExamPerfectScoreTotal) * 100)
lecExamWs = lecExamPs * 0.30

print("\nLaboratory\n")

#while loop that gets the score for assignment (lab)
print("\nAssignment\n")
labAssList = []
labAssPerfectScoreList = []
labAssTotal = 0
labAssPerfectScoreTotal = 0
labAss = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
labAssPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while labAss >= 0 and labAssPerfectScore >= 0:
    labAssList.append(labAss)
    labAssPerfectScoreList.append(labAssPerfectScore)
    labAssTotal += labAss
    labAssPerfectScoreTotal += labAssPerfectScore
    labAss = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    labAssPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
labAssPs = ((labAssTotal / labAssPerfectScoreTotal) * 100)
labAssWs = labAssPs * 0.15

#while loop that gets the score for project (lab)
print("\nProject\n")
labProjList = []
labProjPerfectScoreList = []
labProjTotal = 0
labProjPerfectScoreTotal = 0
labProj = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
labProjPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while labProj >= 0 and labProjPerfectScore >= 0:
    labProjList.append(labProj)
    labProjPerfectScoreList.append(labProjPerfectScore)
    labProjTotal += labProj
    labProjPerfectScoreTotal += labProjPerfectScore
    labProj = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    labProjPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
labProjPs = ((labProjTotal / labProjPerfectScoreTotal) * 100)
labProjWs = labProjPs * 0.20

#while loop that gets the score for recitation (lab)
print("\nRecitation\n")
labRecitList = []
labRecitPerfectScoreList = []
labRecitTotal = 0
labRecitPerfectScoreTotal = 0
labRecit = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
labRecitPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while labRecit >= 0 and labRecitPerfectScore >= 0:
    labRecitList.append(labRecit)
    labRecitPerfectScoreList.append(labRecitPerfectScore)
    labRecitTotal += labRecit
    labRecitPerfectScoreTotal += labRecitPerfectScore
    labRecit = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    labRecitPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
labRecitPs = ((labRecitTotal / labRecitPerfectScoreTotal) * 100)
labRecitWs = labRecitPs * 0.10

#while loop that gets the score for quiz (lab)
print("\nQuiz\n")
labQuizList = []
labQuizPerfectScoreList = []
labQuizTotal = 0
labQuizPerfectScoreTotal = 0
labQuiz = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
labQuizPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while labQuiz >= 0 and labQuizPerfectScore >= 0:
    labQuizList.append(labQuiz)
    labQuizPerfectScoreList.append(labQuizPerfectScore)
    labQuizTotal += labQuiz
    labQuizPerfectScoreTotal += labQuizPerfectScore
    labQuiz = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    labQuizPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
labQuizPs = ((labQuizTotal / labQuizPerfectScoreTotal) * 100)
labQuizWs = labQuizPs * 0.25

#while loop that gets the score for examination (lab)
print("\nExamination\n")
labExamList = []
labExamPerfectScoreList = []
labExamTotal = 0
labExamPerfectScoreTotal = 0
labExam = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
labExamPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))

while labExam >= 0 and labExamPerfectScore >= 0:
    labExamList.append(labExam)
    labExamPerfectScoreList.append(labExamPerfectScore)
    labExamTotal += labExam
    labExamPerfectScoreTotal += labExamPerfectScore
    labExam = float(input("Enter your score (enter a negative number if you do not have inputs anymore): "))
    labExamPerfectScore = float(input("Enter the perfect score (enter a negative number if you do not have inputs anymore): "))
    
labExamPs = ((labExamTotal / labExamPerfectScoreTotal) * 100)
labExamWs = labExamPs * 0.30

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

#for loop that outputs the scores
print("Assignment (Lecture)")
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
print("------------------------------------")

print(f"Lecture Total: {lecTotal}")
print(f"Laboratory Total: {labTotal}")
print(f"Lecture Final Grade: {lecFinalGrade}")
print(f"Laboratory Final GRade: {labFinalGrade}")
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


































