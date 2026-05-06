print(f'\033[1m Welcome to Student Managment Program \033[0m ')
students = []

def addStudent():
        name = input("Enter student name:")
        age = input("Enter student age:")
        gender = input("Enter student gender:")

        if name != "" and age != "" and gender != "":
            student = {
                "name": name,
                "age": age,
                "gender": gender
            }
            students.append(student)
            view_students()

def view_students():
        print(f'\033[1m List of students \033[0m ')
        print("id", "Name", "Age", "Gender")
        for index,student in enumerate(students):
            print(index,student["name"],student["age"],student["gender"])



while True:
    print("Select an option to do:\n1) Add student\n2) View students\n3) Exit")
    option = input("Enter the value 1, 2 or 3: ")
    if option == "1":
        print("add selected")
        addStudent()
    elif option == "2":
        if len(students) > 0:
            view_students()
        else:
            print("No students found")
    elif option == "3":
        break
    else:
        print("Invalid option")

