from google import genai
import os
from google.genai import types
import time

def timer(secondi, frase):
    for i in range(secondi, 0, -1):
        print(i)
        time.sleep(1)
    print(frase)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])



safety_settings= [    
    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),    
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),    
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),    
    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"), ]

config = types.GenerateContentConfig(
    temperature=0.5,
    max_output_tokens=100,
    system_instruction="""
    Sei un tutor di sicurezza informatica per studenti principianti. 
    Spiega i concetti in modo semplice, con esempi pratici. 
    Se non sai qualcosa, dillo chiaramente.
    """,
    safety_settings= safety_settings
    
)



while True:
    c = input("Tu: ")
    if c.lower() == "esci":
        timer(3, "conversazione terminata!" )
        break

    response = client.models.generate_content(
        model="gemini-flash-latest",  
        contents= c,
        config= config

)

    print(f"Giuseppe IA: \n{response.text}")