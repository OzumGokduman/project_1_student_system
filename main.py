def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                students.append(line.strip())
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open("students.txt", "w") as file:
        for s in students:
            file.write(s + "\n")


def add_student(students):
    name = input("Student name: ")
    number = input("Student number: ")
    students.append(f"{name} - {number}")
    save_students(students)


def remove_student(students):
    number = input("Student number to delete: ")
    new_list = []
    for s in students:
        if number not in s:
            new_list.append(s)
    save_students(new_list)
    return new_list


def list_students(students):
    if len(students) == 0:
        print("No students found.")
    else:
        for s in students:
            print(s)


students = load_students()

while True:
    print("\n1- Add Student")
    print("2- Remove Student")
    print("3- List Students")
    print("4- Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        students = remove_student(students)
    elif choice == "3":
        list_students(students)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
