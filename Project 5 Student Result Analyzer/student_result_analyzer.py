# Project- 5 Student Result Analyzer

class Student:
    def __init__(self, name: str, roll_num: int, marks: list):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

    def total(self) -> float:
        return sum(self.marks)
    
    def average(self) -> float:
        return self.total() / len(self.marks)
    
    def grade(self) -> str:
        avg = self.average()
        match avg:
            case avg if avg >= 90: return "A+"
            case avg if avg >= 80: return "A"
            case avg if avg >= 70: return "B"
            case avg if avg >= 60: return "C"
            case avg if avg >= 50: return "D"
            case _: return "F"

    def result(self) -> str:
        if self.average() >= 50:  # Passing criteria
            return "PASS"
        else:
            return "FAIL"
        
    def display(self):
        print(f"Name: {self.name} , Roll_Number: {self.roll_num}, Marks: {self.marks}")
        print(f"Total: {self.total()}, Average: {self.average()}, Grade: {self.grade()}, Result: {self.result()}")


students = [] # Gloabl List

def add_student():
    global students

    try:
        name = input("Enter Name: ")
        roll_num = int(input("Enter Roll_Number: "))
        if roll_num <= 0:
            raise ValueError ("Roll Number must be Positive")
        
        marks = []
        for i in range(1,6):
            mark = int(input(f"Enter Marks {i}: "))
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be Between 0 to 100")
            marks.append(mark)

        new_student = Student(name, roll_num, marks)
        students.append(new_student)

    except ValueError as e:
        print(f"Error" , e)

    else:
        print("Student Added Successfully!")



def show_students():
    global students

    if len(students) == 0:
        print("No Students Added yet")

    else:
        for num, s in enumerate(students, start=1):
            print(f"Student {num}")
            s.display()


def show_passed_students():
    global students

    passed = [s for s in students if s.result() == "PASS"]  # List Comprehension

    if len(passed) == 0:
        print("No Student have passed yet")
    else:
        for num, s in enumerate(passed, start=1):
            print(f"Passed Student {num}")
            s.display()


def show_top_student():
    global students

    if len(students) == 0:
        print("No students to compare")

    else:
        averages = [s.average() for s in students] # List comprehension

        highest_avg = max(averages)

        for s in students:
            if s.average() == highest_avg:
                print("Top Student:")
                s.display()
                break



def menu():
    print("========== STUDENT RESULT ANALYZER ==========")
    print("1. Add Student\n2. Show Students\n3. Show Passed Students\n4. Show Top Student\n5. Exit")
    print("==============================================")


def main():
    try:
        while True:
            menu()
            choice = int(input("Enter Your Choice: "))

            match choice:
                case 1:
                    add_student()

                case 2:
                    show_students()

                case 3:
                    show_passed_students()

                case 4:
                    show_top_student()

                case 5:
                    print("Exiting")
                    break

                case _:
                    print("Inavlid Choice")

    except ValueError:
        print("Please enter a valid number")

    finally:
        print("=================================")
        print("Program Finished Successfully!")
        print("=================================")

if __name__ == "__main__":
    main()