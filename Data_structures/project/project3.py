
student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}


name = input("Enter a name:\n")

if name in student_marks:
    marks = student_marks[name]
    average = sum(marks) / len(marks)
    print("Average percentage mark:")
    print(int(average))  
else:
    print("Student not found.")
