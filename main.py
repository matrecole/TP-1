def count_word(string):  # trouve le nombre de mots dans une phrase (string)
    wordamnt = len(string.split())  # trouve le nombre de mots en divisant la phrase en une liste de mots
    return print(wordamnt)  # retourne le nombre de mot comme output de la fonction


text = str(input("Entrez une phrase contenant seulement des mots en minuscules: \n"))  #

count_word(text)
