def media_mobile(numeri, n):
    risultati = []
    for i in range(len(numeri)):
        finestra = numeri[max(0, i - n + 1) : i + 1]
        media = sum(finestra) / len(finestra)
        risultati.append(round(media, 2))
    return risultati


numeri = []
n = int(input("Inserisci la dimensione della finestra mobile: "))


while True:
    numero = input("Inserisci un numero (o 'fine' per terminare): ")
    if numero.lower() == 'fine':
        break
    try:
        numeri.append(float(numero))
    except ValueError:
        print("Per favore, inserisci un numero valido.")

output = media_mobile(numeri, n)
print(output)

