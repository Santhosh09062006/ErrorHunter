import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    target = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
 
            guess = int(input("Enter your guess (1-100): "))1
    
 
 
            attempts += 1
            if guess < target:
                print("Too low!")
            elif guess > target:
 
 
            guess = int(input("Enter your guess (1-100): "))  
 
 
 
            attempts += 1
            if guess < target:   
 
                print("Too high!")
            elif guess > target:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.") 
guess_the_number()

def main():
    while True:
        print("\nMenu:")
        print("1. Play Guess the Number")
        print("2. Exit")
        
 
        try:
            choice = input("Enter your choice: ")
            if choice in (1,2):
                break
            else:
                print("Enter either 1 or 2")
        except:
            print("Enter either 1 or 2")   
 
        choice = int(input("Enter your choice: "))   
 
        
        if choice == "1":
            guess_the_number()
        elif choice == "2":
            print("Thanks for playing!")
        else:
            print("Invalid choice! Please enter 1 to play or 2 to exit.")   

main()
