# -*- coding: utf-8 -*-
def kalkulatorD (prvo, drugo, operacija):
    try:
        prvo = int(prvo)
    except:
        try:
            prvo = float(prvo)
        except ValueError:
            return ("Nisi vnesel stevila. Ponovi.")
    
    if (operacija == "+" or operacija == "-" or operacija == "*" or operacija == "/"):
        op = True
    else:
        return("Nisi vnesel ustreznega znaka za operacijo. Ponovi.")

    try:
        drugo = int(drugo)
    except:
        try:
            drugo = float(drugo)
        except ValueError:
            return ("Nisi vnesel stevila. Ponovi.")
    rezultat = str(prvo) + operacija + str(drugo)
    return eval(rezultat)
