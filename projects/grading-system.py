student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = 'Outstanding'
    if student_scores[key] in range(81, 91):
        student_grades[key] = 'Exceeds expectations'
    if student_scores[key] in range(71, 81):
        student_grades[key] = 'Acceptable'
    if student_scores[key] < 70:
        student_grades[key] = 'Fail'


# 🚨 Don't change the code below 👇
print(student_grades)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)


result = outer_function(5, 10)
print(result)
