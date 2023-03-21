from random import randrange

map_palab = {"chile": ["agarras", "meto", "sientate", "embarro"],
             "grande": ["agarras", "meto", "sientate", "embarro"],
             "larga": ["agarras", "meto", "sientate", "embarro"],
             "largo": ["agarras", "meto", "sientate", "embarro"],
             "pajaro": ["agarras", "meto", "sientate", "embarro"],
             "pájaro": ["agarras", "meto", "sientate", "embarro"],
             "tronco": ["agarras", "meto", "sientate", "embarro"],
             "camaron": ["agarras", "meto", "sientate", "embarro"],
             "camarón": ["agarras", "meto", "sientate", "embarro"],
             "pepino": ["agarras", "meto", "sientate", "embarro"],
             "elote": ["agarras", "meto", "sientate", "embarro"],
             "birote": ["agarras", "meto", "sientate", "embarro"],
             "chorizo": ["agarras", "meto", "sientate", "embarro"],
             "presta": ["grande"],
             "meto": ["metete"],
             "chico": ["trueno", "como", "me das", "hago", "pasas"],
             "chiquito": ["trueno", "como", "me das", "hago"],
             "atrás": ["trueno", "como", "me das", "hago"],
             "atras": ["trueno", "como", "me das", "hago"],
             "leche": ["sacas", "embarro"],
             "blanco": ["sacas", "embarro"],
             "chispas": ["sacas", "embarro"],
             "crema": ["sacas", "embarro"],
             "chaqueta": ["haces", "me das"],
             "mano": ["haces", "me das"],
             "cabeza": ["agarras", "meto"],
             "piernas": ["alzo"],
             "panza": ["hago"],
             "pancita": ["hago"],
             "hermana": ["prestas", "pasas", "hago"],
             "pulmón": ["tallo"],
             "lomo": ["tallo"],
             "papaya": ["trueno", "como", "exprimo", "me das"], #concha, dona
             "concha": ["trueno", "como", "exprimo", "me das"],
             "dona": ["trueno", "como", "exprimo", "me das"],
             "tripa": ["trueno"],
             "calabaza": ["exprimo", "saco", "embarras"],
             "cacahuate": ["exprimo", "saco", "embarras"],
             "cacahuates": ["exprimo", "saco", "embarras"],
             "frijoles": ["exprimo", "saco", "embarras"],
             "café": ["exprimo", "saco", "embarras"],
             "cafe": ["exprimo", "saco", "embarras"],
             "café": ["exprimo", "saco", "embarras"],
             "cafecito": ["exprimo", "saco", "embarras"],
             "mismo": ["mismo"]
             }

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
            "como": ["¿cómo crees, en serio?", "cómo no se me ocurrió antes!"],
            "exprimo": ["es primero del mes?", "¿es primo suyo el sujeto de ahí?"],
            "saco": ["saco a concluir que tienes razón", "te saco una foto?", "en saco o en costal?", "pues a correr!"],
            "embarras": ["en barras o en tiras?", "en barras de cárcel?", "en Barras, Coahuila"],
            "me das": ["medallones", "me das miedo", "me das tiempo de pensar?"],
            "sacas": ["sácame de una duda", "me sacas de onda", "sácame al sol"],
            "tallo": ["ta' lloviendo", "un tallón de limpieza"],
            "sientate": ["te sientes agusto","siéntate, te veo cansado","siéntate a esperar","siéntate, ahorita te lo paso", "te gusta a ti eso?"],
            "mismo": ["no es lo mismo la cómoda de tu hermana, que acomódame a tu hermana", "no es lo mismo chicas, préstenme el piano, que chicas, présteneme el chicaspiano", "no es lo mismo la papaya tapatía, que tia, tápate la papaya","no es lo mismo un metro de encaje negro, a que un negro te encaje el metro"],
            }

def parse_text(text):
    for word in text.split(" "):
        if map_palab.get(word) != None:
            possib = map_palab.get(word)
            index = randrange(len(possib))
            responses = map_cont[possib[index]]
            index = randrange(len(responses))
            return responses[index]

    return None

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