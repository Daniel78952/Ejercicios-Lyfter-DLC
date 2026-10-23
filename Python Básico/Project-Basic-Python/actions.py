class NoBiggerThanHundredOrLowerThanZero(Exception):
        def __init__(self, message="El número debe estar entre 0 y 100."):
            super().__init__(message)

def age():    # this function will ask for the student's age and validate that it is a number
    while True:
        try:
            student_age = int(input('Digite la edad del estudiante: '))
            break
        except ValueError:
            print("Debe digitar un número, no usar letras")
    return student_age

def grades(subject):    # this function will ask for the student's grade for every subject and validate that it is a number between 0 and 100
    while True:
        try:
            student_grade = float(input(f"Digite la nota de {subject} del estudiante: "))

            if not (0 <= student_grade <= 100):
                raise NoBiggerThanHundredOrLowerThanZero()

            return student_grade

        except NoBiggerThanHundredOrLowerThanZero as error:
            print(error)

        except ValueError:
            print("Debe digitar un número, no usar letras")


def new_students():    # this function asks for students until the user types "salir", returns the list
    students = []
    while True:
        student_name = input('Escriba el nombre completo del estudiante o "salir" para terminar: ')
        if student_name.lower() == 'salir':
            break

        student_age = age()
        student_spanish_grade = grades("español")
        student_science_grade = grades("ciencias")
        student_english_grade = grades("inglés")
        student_social_studies_grade = grades("estudios sociales")
        student_section = input('Escriba la sección del estudiante: ')

        student_info = {
            "name": student_name,
            "age": student_age,
            "spanish_grade": student_spanish_grade,
            "science_grade": student_science_grade,
            "english_grade": student_english_grade,
            "social_studies_grade": student_social_studies_grade,
            "section": student_section
        }

        students.append(student_info)
    return students

def view_students(students):    # this function will display the list of students
    if not students:
        print("No hay estudiantes para mostrar.")
        return

    print("Información de los estudiantes:")
    for number, student in enumerate(students, start=1):
        print(f"\nEstudiante {number}")
        print(f"  Nombre: {student['name']}")
        print(f"  Edad: {student['age']}")
        print(f"  Sección: {student['section']}")
        print(f"  Español: {student['spanish_grade']}")
        print(f"  Ciencias: {student['science_grade']}")
        print(f"  Inglés: {student['english_grade']}")
        print(f"  Sociales: {student['social_studies_grade']}")

def calculate_average(student):    # this will calculate averages for the the functions that need it
    average = (student['spanish_grade'] + student['science_grade'] + student['english_grade'] + student['social_studies_grade']) / 4
    return average

def top_3_students(students):    # this function will display the top 3 students with the best average
    if not students:
        print("No hay estudiantes para mostrar.")
        return

    students_with_average = []
    for student in students:
        average = calculate_average(student)
        students_with_average.append((student, average))

    top_students = sorted(students_with_average, key=lambda x: x[1], reverse=True)[:3]     # x  means student, x[1] means average

    print("Top 3 estudiantes con mejor promedio:")
    for number, (student, average) in enumerate(top_students, start=1):
        print(f"\nEstudiante {number}")
        print(f"  Nombre: {student['name']}")
        print(f"  Promedio: {average:.2f}")

def average_of_all_students(students):    # this function will show the average of all students
    if not students:
        print("No hay estudiantes para mostrar.")
        return

    students_with_average = []
    total = 0
    for student in students:
        average = calculate_average(student)
        students_with_average.append((student, average))
        total += average

    general_average = total / len(students)
    print(f"\nPromedio general de todos los estudiantes: {general_average:.2f}")
    
    print("Los promedios de cada estudiante son los siguientes: ")

    for number, (student, average) in enumerate(students_with_average, start=1):
        print(f"\nEstudiante {number}")
        print(f"  Nombre: {student['name']}")
        print(f"  Promedio: {average:.2f}")