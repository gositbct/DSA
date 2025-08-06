class Student:
    def __init__(self, idn, name, grade):
        self.idn = idn
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"ID: {self.idn}, Name: {self.name}, Grade: {self.grade}"
    

students = [Student(1,'Alice',95.5), Student(2,'Bob',82.0)]

def add_student():
    try:
        idn = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        student = Student(idn, name, grade)
        students.append(student)
        print(f"Student added: {student}")
    except ValueError:
        print("Invalid input. Please try again.")

def search_student():
    try:
        idn = int(input("Enter ID to search: "))
        for student in students:
            if student.idn == idn:
                print(f"Student found: {student}")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid ID.")

def delete_student():
    try:
        idn = int(input("Enter ID to delete: "))
        for i, student in enumerate(students):
            if student.idn == idn:
                removed = students.pop(i)
                print(f"Student deleted: {removed}")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid ID.")

def show_all_students():
    if not students:
        print("No student records.")
    else:
        print("\nAll Students:")
        for s in students:
            print(s)

def menu():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. Search Student by ID")
        print("3. Delete Student by ID")
        print("4. Show All Students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            show_all_students()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

# Start the menu
menu()
