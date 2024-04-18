markes = int(input("Enter your markes: "))
grade = ""
if(markes>100):
    grade = "Invalid Input"
elif(markes<=100 and markes>=80):
    grade = "A+"
elif(markes<80 and markes>=75):
    grade = "A"
elif(markes<75 and markes>=70):
    grade = "A-"
elif(markes<70 and markes>=65):
    grade = "B+"
elif(markes<65 and markes>=60):
    grade = "B"
elif(markes<60 and markes>=55):
    grade = "B-"
elif(markes<55 and markes>=50):
    grade = "C+"
elif(markes<50 and markes>=45):
    grade = "C"
elif(markes<45 and markes>=40):
    grade = "C-"
else:
    grade="F"

print("Your grade (Dependes on your input): ",grade)