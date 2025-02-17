print( "Ciao! Facciamo un quiz. ")
risposta = int(input( "In che anno è nato Alessandro Manzoni? "))
if risposta > 1785:
    print( "Uhm… è nato prima dell anno ",risposta)
    risposta2 = input( "Vuoi studiare di più? Rispondi sì o no ")
    if risposta2 == "sì":
        print( "Ottimo. ")
    else:   
        print( "Ti conviene farlo ugualmente. ")
        if risposta < 1785 :
            print( "Uhm… è nato dopo dell’anno ",risposta)
else:
    print( "Bene. Hai inserito l’anno corretto. ")
print( "A presto. ")