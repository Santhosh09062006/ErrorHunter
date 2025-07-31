# Leap Year or Not: Write a program to determine whether a given year is a leap year.
def is_leap_year(year):
 
    if year % 4 == 0:
        print("leap year")
    else:
        print("not a leap year")

if __name__ == "__main__":
    
    num = int(input("Enter the number :"))
    is_leap_year(num)
 
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:   
 
        return "Leap Year"
    else:   
 
        return "Not a Leap Year"
 