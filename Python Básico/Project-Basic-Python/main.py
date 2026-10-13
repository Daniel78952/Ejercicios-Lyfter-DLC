import menu
import actions
import data

CSV_FILE = 'students.csv'


def main():
    students = []
    while True:
        choice = menu.menu()
        if choice == '1':
            students.extend(actions.new_students())
        elif choice == '2':
            actions.view_students(students)
        elif choice == '3':
            actions.top_3_students(students)
        elif choice == '4':
            actions.average_of_all_students(students)
        elif choice == '5':
            data.export_students_to_csv(CSV_FILE, students)
        elif choice == '6':
            imported = data.import_students_csv(CSV_FILE)
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


if __name__ == "__main__":
    main()