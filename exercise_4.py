#Name: Irish B De Guzman
#Date: November 4, 2025
#Title: Grades Computation
print("Welcome to Grades Computation\n\nClass Standing (Lecture) 70%\n")

# inputs the grades for class standing (lecture)
lecAss = float(input("Enter your assignment grade (15%): "))
lecProj = float(input("Enter your project grade (20%): "))
lecRecit = float(input("Enter your recitation grade (10%): "))
lecQuiz = float(input("Enter your quiz grade (25%): "))

print("\nExamination (Lecture) 30%\n")

#inputs the grade for examination (lecture)
lecExam = float(input("Enter your examination grade (30%): "))

print("\nClass Standing (Laboratory) 70%\n")

#inputs the grade for class standing (lab)
labAss = float(input("Enter your assignment grade (15%): "))
labProj = float(input("Enter your project grade (20%): "))
labRecit = float(input("Enter your recitation grade (10%): "))
labQuiz = float(input("Enter your quiz grade (25%): "))

print("\nExamination (30%)\n")

#inputs the grade for examination (lab)
labExam = float(input("Enter your examination grade (30%): "))

print("\nFinal Grade Lecture (70%) + Laboratory\n")

#initializes the value of perfect score
perfectScore = 100

#computes the percentage score (lecture)
lecAssPs = (lecAss / perfectScore) * 100
lecProjPs = (lecProj / perfectScore) * 100
lecRecitPs = (lecRecit / perfectScore) * 100
lecQuizPs = (lecQuiz / perfectScore) * 100
lecExamPs = (lecExam / perfectScore) * 100

#computes the weighted score (lecture)
lecAssWs = lecAssPs * 0.15
lecProjWs = lecProjPs * 0.20
lecRecitWs = lecRecitPs * 0.10
lecQuizWs = lecQuizPs * 0.25
lecExamWs = lecExamPs * 0.30

#total of class standing (lecture) grade
lecTotalCs = (lecAssWs + lecProjWs + lecRecitWs + lecQuizWs) 

#computes the final (lecture) grade
finalLecture = lecExamWs + lecTotalCs

#computes the percentage score (lab)
labAssPs = (labAss / perfectScore) * 100
labProjPs = (labProj / perfectScore) * 100
labRecitPs = (labRecit / perfectScore) * 100
labQuizPs = (labQuiz / perfectScore) * 100
labExamPs = (labExam / perfectScore) * 100

#computes the weighted score (lab)
labAssWs = labAssPs * 0.15
labProjWs = labProjPs * 0.20
labRecitWs = labRecitPs * 0.10
labQuizWs = labQuizPs * 0.25
labExamWs = labExamPs * 0.30

#total of class standing (lab) grade
labTotalCs = (labAssWs + labProjWs + labRecitWs + labQuizWs) 

#computes the final (lab) grade
finalLab = labExamWs + labTotalCs

#computes the final grade
finalGrade = (finalLecture * 0.70) + (finalLab * 0.30)

#rounds off the final grade to the nearest hundreths
roundedFinalGrade = round(finalGrade, 2)
roundFinalGrade = (roundedFinalGrade + 0.5)

print("Final lecture: ", finalLecture)
print("Final lab: ", finalLab)

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