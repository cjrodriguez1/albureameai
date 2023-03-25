import os
import json
from random import randrange

mmap = {}
map_cont = {} # <--- mapa para las contestaciones
def get_map_palab(filename, value):
    file_palab = open(filename, "r", encoding='utf-8')
    for line in file_palab:
        all_words = line.split(",")
        for word in all_words:
            word = word.strip()
            if len(word) > 1:
                mmap[word.strip()] = value
    file_palab.close()

def populate_map(directory_name):
    directory = os.fsencode(directory_name)
    for file in os.listdir(directory):
        filename = os.fsencode(file).decode()
        value_word = filename.split(".")[0]
        get_map_palab(directory_name + "/" + filename, value_word)

populate_map("palabras")

map_palab = {"nepe": ["agarras", "meto", "sientate", "embarro"],
             "presta": ["grande"],
             "meto": ["metete"],
             "chico": ["trueno", "como", "me das", "hago", "pasas"],
             "blanco": ["sacas", "embarro"],
             "chaqueta": ["haces", "me das"],
             "mano": ["haces", "me das"],
             "cabeza": ["agarras", "meto"],
             "piernas": ["alzo"],
             "panza": ["hago"],
             "pancita": ["hago"],
             "hermana": ["prestas", "pasas", "hago", "empino"],
             "pulmón": ["tallo"],
             "lomo": ["tallo"],
             "concha": ["trueno", "como", "exprimo", "me das"],
             "tripa": ["trueno"],
             "cafe": ["exprimo", "saco", "embarras"],
             "mismo": ["mismo"],
             "nabos": ["agarras", "tallas"]
             }
def populate_map_cont(directory_name):
    with open(directory_name, encoding='utf-8') as f:
        data = json.load(f)
    for key in data:
        map_cont[key] = data[key]

populate_map_cont("contestaciones/contextos.json")

'''
map_cont = {"agarras": ["agárrame que me caigo", "me agarras descuidado", "me tomas la palabra", "me agarraste desprevenido"],
            "sumo": ["asumo que tienes razón", "su moronga joven", "te resumo los hechos", "en su molcajete", "su humilde morada"],
            "meto": ["me torcí un dedo", "me toca de nuevo", "me tocas el vals" "te meto en problemas"],
            "alzo": ["al zócalo", "al zorrillo lo mataron"],
            "pongo": ["te pongo en problemas", "te pongo en aprietos"],
            "empino": ["en Pino Suárez"],
            "grande": ["te brindo la grande", "pues, a la larga te acostumbras", "que milargo que dices algo", "está pelón lo que dices"],
            "embarro": ["en barro sabe mejor", "en barrotes de cárcel", "en cajones también"],
            "haces": ["me haces el gran favor", "dos pa' llevar y una para comer aquí", "hazme el paro", "hazme la buena!"],
            "prestas": ["mejor presta atención", "dame la razón"],
            "metete": ["mejor métete de doctor", "te metes los de dulce", "métete atrás de la fila"],
            "pasas": ["¿cómo pasas a creer?", "pasa a lo siguiente", "mejor échame la culpa", "échame las llaves!", "te pasas de lanza"],
            "hago": ["te hago un tecito", "te hago un favor", "te hago tu malteada", "Santiago", "en Agosto"],
            "trueno": ["todo re bien tostado", "reviento de alegría", "rompo en llanto al oir eso", "a travieso nadie me gana!", "ah, travieso el muchacho!"],
            "como": ["¿cómo crees, en serio?", "cómo no se me ocurrió antes!", "como que andas medio incoherente hoy"],
            "exprimo": ["es primero del mes?", "¿es primo suyo el sujeto de ahí?"],
            "saco": ["saco a concluir que tienes razón", "te saco una foto?", "en saco o en costal?", "pues a correr!", "allá en Apizaco"],
            "embarras": ["en barras o en tiras?", "en barras de cárcel?", "en Barras, Coahuila"],
            "me das": ["medallones", "me das miedo", "me das tiempo de pensar?"],
            "sacas": ["sácame de una duda", "me sacas de onda", "sácame al sol", "¿Conoces a Zacarías?", "en Zacatecas hay muchos de esos"],
            "tallo": ["ta' lloviendo", "un tallón de limpieza"],
            "tallas": ["hay tallas grandes para que te queden mejor", "con limas y limones", "me hueles a cebolla, qué comiste?"],
            "sientate": ["te sientes agusto","siéntate, te veo cansado","siéntate a esperar","siéntate, ahorita te lo paso", "te gusta a ti eso?"],
            "mismo": ["no es lo mismo la cómoda de tu hermana, que acomódame a tu hermana", "no es lo mismo chicas, préstenme el piano, que chicas, présteneme el chicaspiano", "no es lo mismo la papaya tapatía, que tia, tápate la papaya","no es lo mismo un metro de encaje negro, a que un negro te encaje el metro"],
            }
'''

comodines = ["Voy a Palmas, si me haces ese favor", "Cuando compito, compito duro", "El Pájaro con suelas", "No imaginé ver hijas tan grandes!", "Leche de Zacatecas para que te nutras bien", "Sácame de una duda", "En Pino Suárez te dejo y paso por ti luego", "A tu hermana no la he visto"]

def parse_text(text):
    for word in text.split(" "):
        if mmap.get(word) != None:
            possib = map_palab.get(mmap.get(word))
            index = randrange(len(possib))
            responses = map_cont[possib[index]]
            index = randrange(len(responses))
            return responses[index]
        elif map_palab.get(word) != None:
            possib = map_palab.get(word)
            index = randrange(len(possib))
            responses = map_cont[possib[index]]
            index = randrange(len(responses))
            return responses[index]

    return None
    '''
    for word in text.split(" "):
    return None
    '''

text = input("Comencemos: ")
nuevas = []
while(text != "EXIT"):
    resp = parse_text(text)
    if resp != None:
        print(resp)
    else:
        print("No tengo contestacion para: '{}'".format(text))
        nuevas.append(text)
    text = input(">: ")

print("Gracias por participar")
print("Las frases nuevas: {}".format(nuevas))
print(map_cont)

'''
with open("contestaciones/interpretaciones.json", "w", encoding='utf-8') as f:
    json.dump(map_palab, f, ensure_ascii=False, indent=4)
'''