#Student marks & grade checker

print("Student Marks & Grade Checker.")
print("........................")

#ask for student name & number of subjects
name = input("Enter Your Name: ")
sub = int(input("Enter the Number of Subjects: "))

#ask for maximum marks per subject
max_marks = float(input("Enter Maximum Marks of each subject: "))

#total marks and obtained marks
Total = sub * max_marks
obt = 0

#get marks of each subject
for i in range(sub):
    marks = float(input(f"  Enter marks of subject {i+1}: "))
    obt = obt + marks

print(f"Marks: {obt}/{Total}")

#calcukate the percentage
percent = (obt * 100)/Total

#determine grade
if(percent >= 80):
    grade = "A+"
elif(percent >= 70):
    grade = "A-"
elif(percent >= 60):
    grade = "B"
elif(percent >= 50):
    grade = "C"
elif(percent >= 40):
    grade = "D"
elif(percent >= 33):
    grade = "F"
else:
    grade = "F"


#display the result
print(" ")
print("-------RESULT-------")
print(" ")
print(f"Student Name: {name}")
print(f"Total Marks: {Total}")
print(f"Obtained Marks: {obt}")
print(f"Percentage: {percent}")
print(f"Grade: {grade}")


#print(f"Marks: {obt}/{Total} with percentage: {percent}")


