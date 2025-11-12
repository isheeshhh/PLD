#Name: Irish B De Guzman
#Date: November 4, 2025
#Title: Grades Computation
print("Welcome to Grades Computation\n\nClass Standing (Lecture) 70%\n")

# inputs the grades for class standing (lecture)
lecAss = int(input("Enter your assignment grade (15%): "))
lecProj = int(input("Enter your project grade (20%): "))
lecRecit = int(input("Enter your recitation grade (10%): "))
lecQuiz = int(input("Enter your quiz grade (25%): "))

print("\nExamination (Lecture) 30%\n")

#inputs the grade for examination (lecture)
lecExam = int(input("Enter your  examination grade (30%): "))

print("\nClass Standing (Laboratory) 70%\n")

#inputs the grade for class standing (lab)
labAss = int(input("Enter your assignment grade (15%): "))
labProj = int(input("Enter your project grade (20%): "))
labRecit = int(input("Enter your recitation grade (10%): "))
labQuiz = int(input("Enter your quiz grade (25%): "))

print("\nExamination (30%)\n")

#inputs the grade for examination (lab)
labExam = int(input("Enter your examination grade (30%): "))

print("Final Grade Lecture (70%) + Laboratory")

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

print("Final lecture: ", finalLecture)
print("Final lab: ", finalLab)

#outputs the final grade and remarks
if roundedFinalGrade >= 75:
    print("Your final grade is ", roundedFinalGrade, ".", " You passed!")
else:
    print("Your final grade is ", roundedFinalGrade, ".", " You failed!")
