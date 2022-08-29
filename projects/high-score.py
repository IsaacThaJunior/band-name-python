student_scores = input('Input a list of student scores separted by space: ').split(' ')
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)


sum = 0
for score in student_scores:
    if score > sum:
        sum = score


print('The highest score is: ', sum)

