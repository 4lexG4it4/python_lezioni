prezzo_kg = float(input("Inserisci il prezzo al kg delle pesche: "))
kg_acquistati = float(input("Inserisci i kg di pesche acquistati: "))
totale = prezzo_kg * kg_acquistati
print("Totale da pagare:", totale, "euro")
pagato = float(input("Inserisci l'importo pagato dal cliente: "))
resto = pagato - totale
print("Il resto da dare al cliente è:", resto, "euro")
