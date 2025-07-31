class Grades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student, grade):
        self.grades[student] = grade
        print(student,"Grade is ",self.grades[student])
    def calculate_average(self):
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return average

# Example Usage
grades = Grades()
grades.add_grade("John", 85)
grades.add_grade("Sarah", 90)
grades.add_grade("Mike", 78)
print("Average grade:", grades.calculate_average())  