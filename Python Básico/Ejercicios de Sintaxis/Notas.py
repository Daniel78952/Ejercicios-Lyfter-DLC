grade_counter = 1
approved_grades = 0
failed_grades = 0
grade_average = 0
approved_grades_average = 0
failed_grades_average = 0

amount_of_grades = int(input("¿Cúantas notas desea evaluar?: "))
print()
while grade_counter <= amount_of_grades:
    grade = int(input(f"Digite su nota número {grade_counter}: "))
    grade_counter = grade_counter + 1
    if grade < 70:
        failed_grades = failed_grades + 1
        failed_grades_average = failed_grades_average + grade
    else:
        approved_grades = approved_grades + 1
        approved_grades_average = approved_grades_average + grade
    grade_average = grade_average + (grade / amount_of_grades)
if failed_grades > 0:
    failed_grades_average = failed_grades_average / failed_grades
else:
    failed_grades_average = 0

if approved_grades > 0:
    approved_grades_average = approved_grades_average / approved_grades
else:
    approved_grades_average = 0
print()
print(f"El estudiante aprovó {approved_grades} notas y su porcentaje de aprovadas es de {approved_grades_average}.")
print()
print(f"El estudiante reprobó {failed_grades} notas y su porcentaje de desaprovadas es de {failed_grades_average}.")
print()
print(f"Su promedio general es de {grade_average}")
print()
print("¡Fue un placer ayudar!")