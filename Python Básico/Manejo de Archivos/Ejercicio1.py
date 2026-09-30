def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines()

def sort_songs(path, songs):
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(songs)


songs = read_file_by_lines('Ejercicios Python/Manejo de Archivos/canciones.txt')
space_delete = [song.strip() for song in songs]
sorted_songs = sorted(space_delete)
add_space = [song + "\n" for song in sorted_songs]
sort_songs('Ejercicios Python/Manejo de Archivos/mejores_canciones.txt', add_space)