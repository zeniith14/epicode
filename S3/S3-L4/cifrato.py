import base64
import codecs




messaggio = "HSNFRGH".lower()



Alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "z"]

kay = 3



for m in messaggio.lower():
    posizione = Alfabeto.index(m)
    numero = posizione - kay
    print(Alfabeto[numero])
    
        

dacifrare = "QWJhIHZ6b2VidHl2bmdyIHB1ciB6ciBhciBucHBiZXRi"


# Step 1: Base64 decode
decoded = base64.b64decode(dacifrare).decode()

# Step 2: ROT13
final = codecs.decode(decoded, 'rot_13')

print(final)