def student_record_menu():
        students = {}  # Dictionary to store student records

        while True:
            print("\n1. Add Student Record")
            print("2. Display All Records")
            print("3. Search Student by Roll Number")
            print("4. Delete Student Record")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

 

            if choice == 1:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))  #input type changed to int
                students[roll] = (name, marks)       #the key is changed to roll no and the values are names and marks as tuples
            elif choice == 2:
                for roll, details in students.items():
                    print(f"Roll: {roll}, Name: {details[0]}, Marks: {details[1]}")  
            elif choice == 3:
                roll = input("Enter Roll Number to Search: ")
                if roll in students:
                    print(f"Name: {students[roll][0]}, Marks: {students[roll][1]}")
                else:
                    print("Record Not Found")        #else record found --> record not found 
            elif choice == 4:
                roll = input("Enter Roll Number to Delete: ")
                if roll in students:
                    del students[roll]
                    print("Record Deleted")
                else:
                    print("Error occured")           #changed to correct message
            elif choice == 5:
                print("Exiting...")
                break


student_record_menu()       #function call made
 
        if choice == 1:
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
 
            students[name] = (roll, marks)  
        elif choice == 2:
            for details in students.keys():
                print(details," : roll no",students[details][0],"mark ",students[details][1])  
        elif choice == 3:
            roll = input("Enter Roll Number to Search: ")
            for i in students.values():
                if roll in i[0] or [1]:
                    print( next( j for j in students.keys() if students[j][0] == roll))
                else:
                    print("Record not Found")   
        elif choice == 4:
            roll =input("Enter Roll Number to Delete: ")
            a=""
            for i in students:
                
                if students[i][0]==roll:
                    a+=i
                else:
                    print("record not found")
            del students[a]
            print(students)
 
            students[roll] = (name, marks)     
        elif choice == 2:
            for roll, details in students.items():
 
        elif choice == 3:
            roll = input("Enter Roll Number to Search: ")
            if roll in students:
                print(f"Name: {students[details][0]}, Marks: {students[roll][1]}")
            else:
                print("Record Found")   
        elif choice == 4:
            roll = input("Enter Roll Number to Delete: ")
            if roll in students:
                del students[details[0]]
                print("Record Deleted")
            else:
                print("Record Deleted Successfully") 
 
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
 
 
