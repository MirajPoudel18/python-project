# Create a Python program that manages student
# records using a CSV file. The program should
# be able to do the following:
#
#   1. Add new students with their name and
#      grade to a CSV file.
#   2. View all existing student records stored
#      in the CSV file.
#   3. Calculate the average grade of all
#      students in the class.
#   4. Find and display the top scorer
#      (student with the highest grade).
#   5. Exit the program.

question=input(" 1. Add new students with their name and grade to a CSV file. \n "
"2. View all existing student records stored in the CSV file. \n" 
" 3. Calculate the average grade of all students in the class. \n"
 " 4. Find and display the top scorer student with the highest grade.\n"
  "5. Exit the program.\n"
)

#   1. Add new students with their name and grade to a CSV file.
if question == "1":
    Name= input("enter your name")
    grade= input("enter your grade")
    with open("student.csv","a") as f:
        f.write(Name+","+grade +"\n")
        print("Student added successfully!")

#   2. View all existing student records stored in the CSV file.
elif question == "2":
    
    with open("student.csv") as f:
        print(f.read())

#   3. Calculate the average grade of all students in the class.
elif question == "3":
    with open("student.csv", "r") as f:
        next(f)                          # Skip the header line
        total = 0
        i = 0
        for line in f:
            line = line.strip()          # Remove extra spaces and \n
            part = line.split(",")
            grade = int(part[1])         # Get the grade

            total = total + grade
            i += 1

        if i > 0:                        # Check if there are any students
            avg = total / i
            print(f"Average grade of class is {avg}")
        else:
            print("No students found.")



#   4. Find and display the top scorer(student with the highest grade).
elif question == "4":
   with open("student.csv", "r") as f:
        next(f)         # Skip the header line
        
        grade=0       
        
        i = 0
        for line in f:
            line = line.strip()          # Remove extra spaces and \n
            part = line.split(",")
            if grade < int(part[1])  :
                name=  part[0] 
                grade= int(part[1] )

        print(f"{name} scored the highest marks :{grade}")  



#   5. Exit the program.
elif question == "5":
    print("thanks")
    exit

