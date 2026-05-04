print(f'\033[1m Welcome to Student Managment Program\n \033[0m ')
print("Select an option to do:\n1) Add student\n2) View students")
option = input("Enter the value 1 or 2: ")

if option == "1":
    print("add selected")
elif option == "2":
    print("View selected")
else:
    print("Invalid option")

students = []

def view_students():
    print(f'\033[1m List of students\n \033[0m ')