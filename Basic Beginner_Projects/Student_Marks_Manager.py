students = {}

def add_students():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

while True:
    add_students()

    choice = input("Add another student? (y/n): ")

    if choice.lower() == "n":
        break

def avg_marks():
    avg = sum(students.values()) / len(students)
    print("Average Marks:", avg)


def highest_marks():
    print("Highest Marks", max(students.values()))


def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        print("Student Found")
        print("Name:", name)
        print("Marks:", students[name])
    else:
        print("Student not found")
        
print(students)
avg_marks()
highest_marks()
search_student()
