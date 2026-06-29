from ast import Lambda


print("STUDENT MANAGEMENT SYSTEM")
students = []
while True:
    print("=====MENU=====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. show Topper")
    print("7. Average Marks")
    print("8. Total Students")
    print("9. exit")
    choice = input("choose an option: ")
    if choice == "1":
        name = input("Enter student's name: ")
        age = int(input("enter student's age: "))
        marks = int(input("enter student's marks: "))
        if age < 0 or age > 100:
            print("invalid age")
        elif marks < 0 or marks > 100:
            print("invalid marks")
        else:
            student = {"name": name,
                       "age": age,
                       "marks": marks
            }
            students.append(student)
            print("student added successfully")
        
    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            print("Student List:")
            for student in students:
                print("--------------------------------")
                print("name:", student["name"])
                print("age:", student["age"])
                print("marks:", student["marks"])
                print("--------------------------------")
                break
    elif choice == "3":
        search_name = input("enter student's name to search: ")
        found = False
        for student in students:
            if student["name"] == search_name:
                print("student found:")
                print("--------------------------------")
                print("name:", student["name"])
                print("age:", student["age"])
                print("marks:", student["marks"])
                print("--------------------------------")
                found = True
                break
        if not found:
            print("student not found")
    
    elif choice == "4":
        update_name = input("enter student's name to update: ")
        found = False
        for student in students:
            if student["name"] == update_name:
                print("student found ----")
                new_name = input("enter new name: ")
                new_age = int(input("enter new age: "))
                new_marks = int(input("enter new marks: "))
                if new_age < 0 or new_age > 100:
                    print("invalid age")
                elif new_marks < 0 or new_marks > 100:
                    print("invalid marks")
                else:
                    student["name"] = new_name
                    student["age"] = new_age
                    student["marks"] = new_marks
                    print("student updated successfully")
                found = True
                break
        if not found:
            print("student not found")

    elif choice == "5":
        delete_name = input("enter student's name to delete: ")
        found = False
        for student in students:
            if student["name"] == delete_name:
                sure = input("are you sure? (yes/no): ")
                if sure == "yes":
                    students.remove(student)
                    print("student deleted successfully")
                else:
                    print("Deletion cancelled")
                found = True
                break
        if not found:
            print("student not found")

    elif choice == "6":
        if len(students) == 0:
            print("No students found")
        else:
            topper = students[0]
            for student in students:
                if student["marks"] > topper["marks"]:
                    topper = student
            print("========== Topper ===========")
            print("--------------------------------")
            print("name:", topper["name"])
            print("age:", topper["age"])
            print("marks:", topper["marks"])
            print("--------------------------------")
    
    elif choice == "7":
        if len(students) == 0:
            print("No students found")
        else:
            total_marks = 0
            for student in students:
                total_marks += student["marks"]
            average_marks = total_marks / len(students)
            print("========== Class Average ===========")
            print("--------------------------------")
            print("Average marks:", average_marks)
            print("--------------------------------")

    elif choice == "8":
        if len(students) == 0:
            print("no students found")
        else:
            print("total students:", len(students))

    elif choice == "9":
        print("exiting the program... see you again!")
        break

    else:
        print("invalid choice, please try again")