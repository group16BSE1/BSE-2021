#Beginning of function
def computegrade(score_mark):
    if score_mark >= 0.9:
        grade = 'A'
    elif score_mark >= 0.8:
        grade = 'B'
    elif score_mark >= 0.7:
        grade = 'C'
    elif score_mark >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade


marks = float(input('Enter score: '))
print(f'Grade: {computegrade(marks)}')


