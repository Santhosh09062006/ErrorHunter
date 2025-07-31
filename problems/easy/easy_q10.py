# Check Palindrome Number: Use a do-while loop to determine if a given number is a palindrome
def is_palindrome(num):
    original = num
 
    res = 0
    while num > 0:
        digits = num % 10
        res = res * 10 + digits
        num //= 10
    return res == original
 
    reverse = 0
 
    do 
    reverse = reverse * 10 + num % 10
    num //= 10
    while num != 0 :
        reverse == original
 
if __name__ == "__main__":
    nums = int(input("Enter the Number: "))
    res = is_palindrome(nums)
 
 
    do:
 
    while num != 0:
        reverse = reverse * 10 + num % 10
 
        num //= 10
    
    return reverse == original
 
 
