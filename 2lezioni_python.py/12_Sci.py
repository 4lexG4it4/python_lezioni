studenti = int(input("Inserisci il numero di studenti: "))
peso_studente = float(input("Inserisci il peso medio di uno studente in kg: "))
peso_extra = 5  
peso_totale = studenti * (peso_studente + peso_extra)
print("Il peso totale trasportato dalla corriera sarà:", peso_totale, "kg")
