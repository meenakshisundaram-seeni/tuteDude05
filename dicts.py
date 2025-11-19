student_marks = {
    "Shakti": 94,
    "Sneha": 96,
    "Akshat": 76,
    "Meenakshi": 69
}

name = input("Enter the student's name: ")

marks = student_marks.get(name)

if marks is not None:
    print(f"{name}'s marks: {marks}")
else:
    print("Student not found.")
