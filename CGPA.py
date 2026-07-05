courses = int(input('How many courses?'))

total_units = 0
total_points = 0

for i in range(courses):
    
    print('\nCourse', i + 1)

    unit = int(input('Courses Unit:'))
    score = int(input('Score:'))

    if score >= 70:
        grade = 'A'
        point = 5

    elif score >= 60:
        grade = 'B'
        point = 4

    elif score >= 50:
        grade = 'C'
        point = 3

    elif score >= 40:
        grade = 'D'
        point = 2

    elif score >= 30:
        grade ='E'
        point = 1

    else:
        grade = 'F'
        point = 0

    quality = point * unit

    total_units += unit
    total_points += quality

    print('Grade:', grade)
    print('Point:', point)

    cgpa = total_points/ total_units

    print('\n===== RESULT =====')
    print('Total Units =', total_units)
    print('Total Quality Points =', total_points)
    print('CGPA =', round(cgpa,2))


