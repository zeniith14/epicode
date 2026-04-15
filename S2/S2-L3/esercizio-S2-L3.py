import math

while True:
    try:
        
        print("1 = Quadrato: \n2 = Cerchio: \n3 = Rettangolo:\n4 = Fine")
        n = int(input("Inserisci un numero intero: "))
        
        # chiusura del programma
        if n == 4:
            print("Programma terminato.")
            break
        
        # quadrato
        if n == 1:
            try:
                lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
                perimetro = lato * 4
                print(f"Il perimetro del quadrato è: {perimetro}")
            except ValueError:
                print("Input non valido. Per favore, inserisci un numero.")
                if n  == str:
                    print("Input non valido. Per favore, inserisci un numero intero.")
        # cerchio
        if n == 2:
            try:
                
                raggio = float(input("Inserisci il raggio del cerchio: "))
                cirfoerneza = 2 * math.pi * raggio 
                print(f"La circonferenza del cerchio è: {cirfoerneza:.2f}")
            except ValueError:
                print("Input non valido. Per favore, inserisci un numero.")
                if n  == str:
                    print("Input non valido. Per favore, inserisci un numero intero.")
        # rettangolo
        if n == 3:
            try:


                base = float(input("Inserisci la lunghezza del rettangolo: "))
                altezza = float(input("Inserisci la larghezza del rettangolo: "))
                perimetro = base * 2 + altezza * 2
                print(f"Il perimetro del rettangolo è: {perimetro:.2f}")
                
            except ValueError:
                print("Input non valido. Per favore, inserisci un numero.")
                if n  == str:
                    print("Input non valido. Per favore, inserisci un numero intero.")
                    

    except ValueError:
        print("Input non valido. Per favore, inserisci un numero intero.")
        if n > 6 or n < 1:
            print("Numero non valido. Per favore, inserisci un numero tra 1 e 4.")