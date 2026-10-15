import csv

def export_students_to_csv(path, students):   # this will export the students data to a csv file
    if not students:
        print("No hay estudiantes para guardar.")
        return
    
    with open(path, 'w', encoding='utf-8-sig', newline='') as file:    # -sig is useful so it can be viewed properly on excel in various devices(tested with, iPhone, PC and Samsung)
        headers = students[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')
        
        writer.writeheader()
        
        writer.writerows(students)
    print("Datos exportados correctamente.")

def import_students_csv(path):    # returns the list of students, or None if the file does not exist
    try:
        with open(path, 'r', encoding='utf-8-sig', newline='') as file:
            students = []
            for row in csv.DictReader(file, delimiter=';'):
                row['age'] = int(row['age'])
                row['spanish_grade'] = float(row['spanish_grade'])
                row['science_grade'] = float(row['science_grade'])
                row['english_grade'] = float(row['english_grade'])
                row['social_studies_grade'] = float(row['social_studies_grade'])
                students.append(row)
            return students
    except (FileNotFoundError, ValueError, KeyError):
        return None