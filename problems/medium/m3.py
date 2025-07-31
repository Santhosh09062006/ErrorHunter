
# solve . Find the bugs and solve it

def string_manipulation_menu():
    print("1. Count Vowels")
    print("2. Reverse String")
    print("3. Check Palindrome")
    print("4. Replace Substring")
 
    choice=int(input("Enter your choice"))
 
    
    choice = int(input("Enter your choice: "))
 
    if choice == 1:
        s = str(input("Enter a string: "))
 
 
    s = input("Enter a string: ")

    if choice == 1:
        vowels = "a","e","i","o","u","A","E","I","O","U"
 
        count = 0
        lst=[]
        for char in s:
            if char in vowels:
 
                count += 1 
        print("Number of Vowels:", count)
    elif choice == 2:
        s = str(input("Enter a string: "))
        print("Reversed String:", s[::-1])  
    elif choice == 3:
        s = str(input("Enter a string: "))
        if s[::-1] != s:
            print("Not a Palindrome")  
 
 
                if char not in lst:
                    count += 1
                    lst.append(char)
        print("Number of Vowels:", count,lst)
    elif choice == 2:
        print("Reversed String:", s[::-1])  
    elif choice == 3:
        if s[::-1] == s:
            print("Palindrome")  
 
        else:
            print("Palindrome")
    elif choice == 4:
 
        s = str(input("Enter a string: "))
        old = input("Substring to replace: ")
        new = input("Replacement substring: ")
        s=s.replace(old,new)
        print("Updated String:", s)   
    else:
        print("Invalid option")
string_manipulation_menu()
 
        srr1=""
        old = input("Substring to replace: ")
        new = input("Replacement substring: ")
        for char in s:
            if char==old:
                new=char
                srr1+=char
            else:
                srr1+=char
            
        print("Updated String:",srr1)   
    else:
        print("Invalid option")

string_manipulation_menu()
 
 
                count += 1 
        print("Number of Vowels:", count)
    elif choice == 2:
        print("Reversed String:", s[::-1])  
    elif choice == 3:
        if s[::-1] == s:
 
                count += 1  
        print("Number of Vowels:", count)
    elif choice == 2:
        print("Reversed String:", s[::-1]) 
    elif choice == 3:
        if s == s[::-1]:  
            print("Palindrome")
 
                count += 1 
        print("Number of Vowels:", count)
    elif choice == 2:
 
        print("Reversed String:", s[::-1])  
 
 
string_manipulation_menu()
 
 