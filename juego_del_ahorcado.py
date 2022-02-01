import random, os


IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


## Función para limpiar pantalla
def clear():
    os.system("cls")


## Función que obtiene las palabras de un archivo externo. 
def read_data():
    list_words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            list_words.append(word.replace("\n", ""))
    
    #select_word = random.choice(list_words)
    #print(select_word)
    return list_words


## Función que compara las letras ingresadas por el usuario con la generada por el código.
def comparison(select_word, spaces):
    compared_word = list(select_word)
    compared_spaces = list(spaces)
    
    while compared_word != compared_spaces:
        user = input("Ingrese una letra: ")

        #assert len(user) >= 0, "Presionaste mas de una letra"
        clear()
        for i in range(0, len(compared_word)):
            if compared_word[i] == user:
                compared_spaces[i] = compared_word[i]
        print(" ".join(compared_spaces).upper())
        print("\n")
    
    print("Ganaste, la palabra era: " + select_word)


## Función principal
def run():
    clear()
    palabra = read_data()
    select_word = random.choice(palabra)
    spaces = ["_"]*len(select_word)
    #attemps = 6
    print("Adivina la palabra")
    print(" ".join(spaces))
    #print(select_word)
    print("\n")

    comparison(select_word, spaces)


if __name__ == "__main__":
    run()