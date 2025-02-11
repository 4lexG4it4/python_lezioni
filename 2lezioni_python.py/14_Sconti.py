prezzo=int(input("inserisci il prezzo della maglietta: "))
prezzo_scontato=prezzo-prezzo*0.20
print("il prezzo scontato è: ", prezzo_scontato)
contanti=int(input("inserisci i contanti: "))
resto=contanti-prezzo_scontato
print("resto: ",resto)