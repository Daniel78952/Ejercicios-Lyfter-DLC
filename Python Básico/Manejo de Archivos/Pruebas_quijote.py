# def read_file_by_lines(path):
#     with open(path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#         # Iteramos sobre la lista de líneas obtenida
#         for number, line in enumerate(lines, start=1):
#             # Usamos strip() para remover los saltos de línea y limpiar espacios
#             print(f"Line {number}: {line.strip()}")

# read_file_by_lines('Ejercicios Python/Manejo de Archivos/quijote.txt')



# def write_new_life(path, text):
#     with open(path, 'w', encoding='utf-8') as file:
#         file.write(text)

# new_text = "Capitulo II. Que trata de la primera salida que su tierra hizo el ingenioso Don Quijote."

# write_new_life("Ejercicios Python/Manejo de Archivos/quijote_capitulo2.txt", new_text)



def append_to_file(path, extra_text):
    with open(path, 'a', encoding='utf-8') as file: #si uso el de write que es "w" en vez de agregar una línea este borra el archivo y crea un nueva linea
        # Añadimos un salto de línea antes del nuevo texto para no pegarlo al anterior
        file.write("\n" + extra_text)

additional_text = "Hechas, pues, estas prevenciones, no quiso aguardar más tiempo a poner en efeto su pensamiento..."

append_to_file('Ejercicios Python/Manejo de Archivos/quijote_capitulo2.txt', additional_text)