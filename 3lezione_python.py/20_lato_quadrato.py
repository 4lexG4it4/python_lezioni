import math
area = float(input("Inserisci l'area del quadrato: "))  #chiede l'area all'utente 
lato = math.sqrt(area)  #calcola il lato
print("Il lato del quadrato è:", round(lato, 1))  #arrotonda alla prima cifra decimale
