meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL ": "Una respuesta común a algo gracioso",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "ROFL": "una respuesta a una broma"
        }
print("hola ")
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("la definición es :", meme_dict[word] )
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No está en la lista")
