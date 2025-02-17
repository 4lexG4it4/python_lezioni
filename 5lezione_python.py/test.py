print("ciao controlliamo come va in informatica")
voto1=float(input("inserisci il primo voto che hai preso:"))
voto2=float(input("inserisci il secondo voto che hai preso:"))
media=(voto1+voto2)/2
if media >= 6:
    print("benissimo procedi cosi")
else:
    if voto2 > voto1:
        print("bene almeno stai migliorando")
    else: 
        print("bisogna recuperare")
print("a presto")