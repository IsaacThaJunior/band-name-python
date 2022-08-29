student_heights = input(
    'Input a list of students heights, separated by space: ').split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

sum = 0
length = 0

for height in student_heights:
    sum += height 

for height in student_heights:
    length += 1


average =round(sum/length)

print(average)