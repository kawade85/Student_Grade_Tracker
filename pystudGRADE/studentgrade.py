1# ### Task 1 - Student Grade Tracker ###

# By using a Dictionary. Dictionary is a collection of 'Key- value' pair.
# Syntax for Dictionary - {key : value, key2 : value}

#here 'Key' will be denoted for Student's name and 'value' for their Grades.
# add,  update,  delete,  view,  exit  student's  information

#initializing the dictionary
stud_grades = { }

# Adding students info
def add_student(name, grade):
    stud_grades[name] = grade
    print (f"Added {name} with a {grade}")

# updating students info
def update_student(name, grade):
    if name in stud_grades:
        stud_grades[name] = grade
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} not found!")

# deleting a students info
def delete_student(name):
    if name in stud_grades:
        print(f"{name} has been successfully deleted!")

    else:
        print(f"{name} is not found!")

#view all students info
def display_all_studs():
    if stud_grades:
        for name, grade in stud_grades.items():
            print(f"{name} : {grade}")
        
        else:
            print("No students found/added !")


# main function

def main_func() :
    while True :
        print("\n ***** Student Grade Tracker System ***** ")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1 :
            name = input("Enter Student's Name : ")
            grade = int(input("Enter Student's Grade : "))
            add_student(name, grade)   #calling function

        elif choice == 2:
            name = input("Enter Student's Name : ")
            grade = int(input("Enter Student's Grade : "))
            update_student(name, grade)    #calling function

        elif choice == 3:
            name = input("Enter Student's Name : ")
            delete_student(name)   #calling function

        elif choice == 4:
            display_all_studs()    #calling function

        elif choice == 5:
              print("Closing the Program...     ")
              break
        
        else : 
            print("Invalid choice")
       
# Run the main function
if __name__ == "__main__":
    main_func()



            
       