print('---Más de 4---')

words_list =[]

for words in range(5):
    user_words = input("Escriba 5 palabras: ")
    words_list.append(user_words)

more_than_4 = []

for letters in words_list:
    if len(letters)>4:
        more_than_4.append(letters)

print(more_than_4)

# cuando quise buscar otras maneras de hacerlo, 
# en internet encontré esto:
# letters for letters in words_list if len(letters) > 4
#lo pongo porque quería saber si esta manera de escribir
# es algo que también vamos a aprende más adelante
# más que todo porque me llama la atención lo efeciente que se ve