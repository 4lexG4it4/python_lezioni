prezzo_jeans1 = float(input("Inserisci il prezzo della prima paia di jeans: "))
prezzo_jeans2 = float(input("Inserisci il prezzo della seconda paia di jeans: "))

prezzo_scontato1 = prezzo_jeans1 - (prezzo_jeans1 * 0.20)
prezzo_scontato2 = prezzo_jeans2 - (prezzo_jeans2 * 0.20)

totale = prezzo_scontato1 + prezzo_scontato2
print("Il totale scontato è:", totale, "euro")

contanti = float(input("Inserisci l'importo pagato dal cliente: "))
resto = contanti - totale
print("Il resto da dare al cliente è:", resto, "euro")
