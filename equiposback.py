
class ping:
    equipo = "pinguinos galacticos"
    inte1 = "Yahir Monje"
    inte2 = "Yesica Rodriguez"
    inte3 = ""
    integrantes = "{} \n {} \n {}".format(inte1, inte2, inte3)

 
class innombrables:
    equipo = "Los =^UwU^="
    inte1 = "Norma Mendoza"
    inte2 = "Jonathan Durán"
    inte3 = "Leonardo Gonzáles"
    integrantes = "{} \n {} \n {}".format(inte1, inte2, inte3)
    

class polys:
    equipo = "PolyStation"
    inte1 = "Ixchel Arreguin"
    inte2 = "Fernando Siqueiros"
    inte3 = ""
    integrantes = "{} \n {} \n {}".format(inte1, inte2, inte3)


class mosqueteros:
    equipo = "Los 3 Mosqueteros"
    inte1 = "Erick Lozano"
    inte2 = "Dania Benavides"
    inte3 = "Ana Valenzuela"
    integrantes = "{} \n {} \n {}".format(inte1, inte2, inte3)
    

class toyota:
    equipo = "Toyotalegacy"
    inte1 = "Mauricio Garcia"
    inte2 = "Elias Sierra"
    inte3 = "Israel Chacon"
    integrantes = "{} \n {} \n {}".format(inte1, inte2, inte3)


class web:
    equipo = "WebHeros"
    inte1 = "Axel Reyes"
    inte2 = "Jesus Arellanos"
    inte3 = "Daniel Delgado"
    integrantes = "{} \n {} \n {}".format(inte1, inte2, inte3)


class fs3:
    print("equipos \n 1-pinguinos galacticos \n 2-innombrables \n 3-polys \n 4-mosqueteros \n 5-toyota \n 6-web")
    opcion = int(input("Selecciona un equipo: "))
    
    if opcion == 1:
        pinguinos = ping()
        print(pinguinos.integrantes)
    if opcion == 2:
        inn = innombrables()
        print(inn.integrantes)
    if opcion == 3:
        pol = polys()
        print(pol.integrantes)
    if opcion == 4:
        mos = mosqueteros()
        print(mos.integrantes)
    if opcion == 5:
        toy = toyota()
        print(toy.integrantes)
    if opcion == 6:
        heros = web()
        print(heros.integrantes)

print(fs3)