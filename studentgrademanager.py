
students = []

# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Function to add a student
def add_student():
    name = input("Enter student name: ")

    marks = {}

    subjects = ["Maths", "Science", "English"]

    for subject in subjects:
        mark = float(input(f"Enter marks in {subject}: "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            return

        marks[subject] = mark

    total = sum(marks.values())
    percentage = total / 3
    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("Student added successfully!")


# Function to display all students
def display_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("\n")
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Percentage:", student["percentage"], "%")
        print("Grade:", student["grade"])


# Function to search for a student
def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Percentage:", student["percentage"], "%")
            print("Grade:", student["grade"])
            return

    print("Student not found.")


# Main program
while True:
    print("\nSTUDENT GRADE MANAGER")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
