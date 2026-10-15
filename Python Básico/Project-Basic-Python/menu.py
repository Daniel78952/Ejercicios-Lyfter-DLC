# import menu
# import actions
# import data

# def menu():
#     print("\nEditor de datos de estudiantes\n")
#     print("Por favor escoja una opción:")
#     print("1. Ingresar información de un estudiante")
#     print("2. Ver información de los estudiantes")
#     print("3. Ver el top 3 estudiantes con mejor promedio")
#     print("4. Ver el promedio de todos los estudiantes")
#     print("5. Exportar información de los estudiantes a un archivo CSV")
#     print("6. Importar información de los estudiantes desde un archivo CSV")
#     print("7. Salir del programa\n")

#     return input("Digite su opción (1-7): ")

# def main():
#     students = []
#     while True:
#         choice = menu.menu()
#         if choice == '1':
#             students.extend(actions.new_students())
#         elif choice == '2':
#             actions.view_students(students)
#         elif choice == '3':
#             actions.top_3_students(students)
#         elif choice == '4':
#             actions.average_of_all_students(students)
#         elif choice == '5':
#             data.export_students_to_csv(CSV_FILE, students)
#         elif choice == '6':
#             imported = data.import_students_csv(CSV_FILE)
#             if imported is None:
#                 print("No se pudo importar: no hay un archivo exportado o el archivo es inválido.")
#             else:
#                 students = imported
#                 print(f"Se importaron {len(students)} estudiantes.")
#         elif choice == '7':
#             print("Se ha cerrado el programa.")
#             break
#         else:
#             print("Opción inválida. Por favor intente otra vez")



import actions
import data


def menu():

    while True:
        print("\nEditor de datos de estudiantes\n")
        print("Por favor escoja una opción:")
        print("1. Ingresar información de un estudiante")
        print("2. Ver información de los estudiantes")
        print("3. Ver el top 3 estudiantes con mejor promedio")
        print("4. Ver el promedio de todos los estudiantes")
        print("5. Exportar información a un archivo CSV")
        print("6. Importar información desde un archivo CSV")
        print("7. Salir del programa\n")

        return input("Digite su opción (1-7): ")

def run_menu():
    students = []
    csv_file = "students.csv"
    while True:
        choice = menu()
        if choice == '1':
            students.extend(actions.new_students())
        elif choice == '2':
            actions.view_students(students)
        elif choice == '3':
            actions.top_3_students(students)
        elif choice == '4':
            actions.average_of_all_students(students)
        elif choice == '5':
            data.export_students_to_csv(csv_file, students)
        elif choice == '6':
            imported = data.import_students_csv(csv_file)
            if imported is None:
                print("No se pudo importar: no hay un archivo exportado o el archivo es inválido.")
            else:
                students = imported
                print(f"Se importaron {len(students)} estudiantes.")
        elif choice == '7':
            print("Se ha cerrado el programa.")
            break
        else:
            print("Opción inválida. Por favor intente otra vez")