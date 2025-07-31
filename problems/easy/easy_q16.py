# Print the Sum of First and Last Array Element
def sum_first_last(arr):
 
    for i in range(len(arr)):
        return arr[0] + arr[-1]  
 
 
    if len(arr) < 2:
        return "Array must have at least two characters."
    return arr[0] + arr[-1]

 
if __name__ == "__main__":
    user = [int(x) for x in (input("Enter a collection number:")).split(",")]
 
    print(sum_first_last(user))
 
 
    arr=int()
    sum_first_last()
 
    arr=[]
    n=int(input("Enter the Total number of Elements:"))
    for i in range(n):
        x=int(input("Enter the element :"))
        arr.append(x)
 
    arr=[2,5,8,7,6]
 
    print(sum_first_last(arr))
 
 