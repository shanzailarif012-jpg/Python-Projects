# 🎓 Student Result Analyzer

A **console-based Student Result Analyzer** built in Python using **Object-Oriented Programming (OOP)**.

This project allows users to add students, store their marks, calculate total and average marks, assign grades, check pass/fail status, display all students, find passed students, and identify the top-performing student.

---

## 🚀 Features

- ➕ Add a new student
- 📝 Store student name, roll number, and marks
- 📊 Calculate total marks
- 📈 Calculate average marks
- 🏆 Automatically assign grades
- ✅ Check PASS / FAIL result
- 👨‍🎓 Display all students
- 🎯 Display only passed students
- 🥇 Find the top student based on average marks
- 🔢 Menu-driven console interface
- ⚠️ Input validation and error handling

---

## 📋 Grade System

| Average Marks | Grade |
|---------------|-------|
| 90 – 100      | A+    |
| 80 – 89       | A     |
| 70 – 79       | B     |
| 60 – 69       | C     |
| 50 – 59       | D     |
| Below 50      | F     |

**Passing Criteria:** Average marks ≥ 50

---

## 🛠️ Technologies Used

- **Python 3**
- Object-Oriented Programming (OOP)
- Classes & Objects
- Constructors
- Instance Methods
- Type Hints
- Lists
- List Comprehension
- `match-case`
- `try-except`
- `raise ValueError`
- `enumerate()`
- Built-in functions like `sum()` and `max()`

---

## 📂 Project Structure

```text
Student-Result-Analyzer/
│
├── student_result_analyzer.py
└── README.md
💻 How It Works

When the program starts, a menu is displayed:

========== STUDENT RESULT ANALYZER ==========
1. Add Student
2. Show Students
3. Show Passed Students
4. Show Top Student
5. Exit
==============================================
1️⃣ Add Student

The program asks for:

Student name
Roll number
Marks of 5 subjects

It validates that:

Roll number is positive
Marks are between 0 and 100
Input values are valid numbers
2️⃣ Show Students

Displays all added students along with:

Name
Roll number
Marks
Total
Average
Grade
Result
3️⃣ Show Passed Students

Uses list comprehension to filter students whose average marks are 50 or above.

4️⃣ Show Top Student

Calculates the average of every student and identifies the student with the highest average.

5️⃣ Exit

Terminates the program safely.

🧠 OOP Implementation

The project uses a Student class to represent each student.

class Student:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

The class contains methods for:

total()
average()
grade()
result()
display()

This keeps student-related data and operations organized inside one class.

⚠️ Error Handling

The project uses try-except and ValueError to handle invalid input.

For example:

if mark < 0 or mark > 100:
    raise ValueError("Marks must be Between 0 to 100")

This prevents invalid marks from being stored.

🎯 Learning Objectives

This project was created to practice and strengthen:

Object-Oriented Programming
Classes and Objects
Methods and Constructors
List Comprehension
Conditional Logic
match-case
Exception Handling
Input Validation
Working with Lists
Building Menu-Driven CLI Applications
▶️ How to Run

Make sure Python 3 is installed.

Clone the repository:

git clone https://github.com/your-username/student-result-analyzer.git

Go into the project directory:

cd student-result-analyzer

Run the program:

python student_result_analyzer.py
📌 Example Output
Student 1
Name: Muhammad, Roll_Number: 101, Marks: [85, 90, 78, 88, 92]

Total: 433
Average: 86.6
Grade: A
Result: PASS
📚 Project Type

CLI / Console-Based Python Project

Built as part of my Python learning and practice journey to strengthen Object-Oriented Programming and real-world problem-solving skills.

👨‍💻 Author

Muhammad Shanzail

Python / Backend Developer

⭐ If you found this project useful, consider giving the repository a star!