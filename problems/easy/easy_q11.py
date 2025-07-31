def day_of_week(day):
 
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
 
    return switch.get(day) 
if __name__ == "__main__":
    num = int(input("Enter a number from 1 to 7:"))
    xcd = day_of_week(num)
    print(xcd)
 
    return switch[day]   
if __name__ == "__main__":
    
    a= day_of_week(7)
    print(a)
 
 
    return switch.get(day)
if __name__ == "__main__":
    day=int(input("Enter day number:"))
    xcd = day_of_week(day)
 
    print(xcd)
  