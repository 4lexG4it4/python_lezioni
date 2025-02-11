"""prezzo=float(input("inserisci il prezzo del biglietto:"))
numero=int(input("inserisci il numero di biglietti acquistati:"))
if numero > 20:
    numero=numero-1
totale=numero*prezzo
print("il totale da pagare è",totale)
"""
prezzo = float(input("Inserisci il prezzo del biglietto: "))
numero = int(input("Inserisci il numero di biglietti acquistati: "))

# Calcoliamo i biglietti omaggio
biglietti_pagati = numero - (numero // 20)  # Ogni 20 biglietti acquistati, uno è omaggio

totale = biglietti_pagati * prezzo
print("Il totale da pagare è:", totale)
