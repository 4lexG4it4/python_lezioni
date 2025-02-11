costo_biglietto = 30  
costo_camera = float(input("Inserisci il costo della camera per notte a studente: "))
notti = int(input("Inserisci il numero di notti di permanenza: "))
costo_totale = costo_biglietto + (costo_camera * notti)
print("Ogni studente deve pagare:", costo_totale, "euro")
