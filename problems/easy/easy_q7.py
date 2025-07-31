def sum_of_digits(num):
    """Calculate the sum of digits of a number."""
    total = 0
    num = abs(num)   
    while num > 0:
 
        total += (num % 10) 
        num //=10
    return total

if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    total=sum_of_digits(num)
    print("Sum of digits:",total)

 
        
 
 
        digits = num%10
        total += digits 
 
        num //= 10
    return total

if __name__ == "__main__":
    number = int(input("Enter the Number : "))
 
    print(sum_of_digits(number))
 
    print("Sum of digits:",sum_of_digits(number))
    
    
    
 
 
        n=num%10
        total+=n
        num=num//10
 
 
        total += num % 10
 
 
        num //= 10  
 
 
    return total

 
        num //= 10          
    return total
 