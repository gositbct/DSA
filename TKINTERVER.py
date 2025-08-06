import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, idn, name, grade):
        self.idn = idn
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"ID: {self.idn}, Name: {self.name}, Grade: {self.grade}"

students = [Student(1, 'Alice', 95.5), (Student(2, 'Bob', 82.0))]

# GUI Functions
def Adding():
    try:
        idn = int(idn_idn.get())
        name = name_name.get()
        grade = float(entry_grade.get())
        student = Student(idn, name, grade)
        students.append(student)
        Clear()
    except ValueError:
        messagebox.showinfo("Invalid ID or Grade")

def Search():
    try:
        idn = int(idn_idn.get())
        for student in students:
            if student.idn == idn:
                messagebox.showinfo("Search Result", str(student))
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid ID")

def Delete():
    try:
        idn = int(idn_idn.get())
        for i, student in enumerate(students):
            if student.idn == idn:
                del students[i]
                Clear()
                messagebox.showinfo("Deleted", f"Deleted: {student}")
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid ID")


def Clear():
    idn_idn.delete(0, tk.END)
    name_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)


assignment1 = tk.Tk()
assignment1.title("Student Record System")
assignment1.geometry("300x200")

# Input Fields
tk.Label(assignment1, text="Student ID:").grid(row=0, column=0, sticky='w')
idn_idn = tk.Entry(assignment1)
idn_idn.grid(row=0, column=1)

tk.Label(assignment1, text="Name:").grid(row=1, column=0, sticky='w')
name_name = tk.Entry(assignment1)
name_name.grid(row=1, column=1)

tk.Label(assignment1, text="Grade:").grid(row=2, column=0, sticky='w')
entry_grade = tk.Entry(assignment1)
entry_grade.grid(row=2, column=1)


tk.Button(assignment1, text="Add", command=Adding).grid(row=3, column=0, pady=5)
tk.Button(assignment1, text="Search", command=Search).grid(row=3, column=1)
tk.Button(assignment1, text="Delete", command=Delete).grid(row=4, column=0)
tk.Button(assignment1, text="Clear", command=Clear).grid(row=4, column=1)




assignment1.mainloop()
