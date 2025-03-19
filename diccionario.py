meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'hola' : 'saludo comun',
            }

palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if palabra in meme_dict.keys():
    
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(palabra)
else:

    print('No existe esa palabra')
