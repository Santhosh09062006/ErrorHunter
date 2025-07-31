 
# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade):
    switch = {
 
        'A': "Excellent",
        'B': "Good",
        'C': "Average",
        'D': "Poor",  
        'B': "Good",
        'C': "Average",
        'D': "Poor",
        'A': "Excellent",  
 
        'F': "Fail"
 
 
    }
 
    return switch.get(grade, "Not a valid grade") 

if __name__ == "__main__":
 
    user = input("Enter grade among A,B,C,D,F *in captial:")
    rs = grade_description(user)
 
    alp = input("Enter a grade: ").upper()
    rs = grade_description(alp)
 
    print(rs)
  