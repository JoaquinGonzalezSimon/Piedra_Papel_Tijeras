#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string1 = """
 ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗██╗
██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║
██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗  ██║
██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝  ╚═╝
╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗██╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝                                                      
"""

string2 = """
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
"""

import random
from enum import IntEnum

class Entrada(IntEnum): #
    Piedra = 0
    Papel = 1
    Tijeras = 2
    Lagartija = 3
    Spock = 4
    
contador_jugador, contador_computadora = 0,0
    
Que_vence_a_que = {
    Entrada.Tijeras: [Entrada.Lagartija, Entrada.Papel],
    Entrada.Papel: [Entrada.Spock, Entrada.Piedra],
    Entrada.Piedra: [Entrada.Lagartija, Entrada.Tijeras],
    Entrada.Lagartija: [Entrada.Spock, Entrada.Papel],
    Entrada.Spock: [Entrada.Tijeras, Entrada.Piedra]
}

def user():
    flag1 = False
    while flag1 == False:
        eleccion_jugador = input("\nSobres we, qué quieres?: 'piedra', 'papel', 'tijeras', 'lagartija' o 'Spock'")
        if eleccion_jugador not in ["0","1","2","3","4"]:
            print("""Tienes que leer compadre! 
              Selecciona 
              '0', para 'piedra, 
              '1', para 'papel', 
              '2' para 'tijera', 
              '3' para 'lagartija', o
              '4' para 'Spock' """)
    
        else:
            flag1 = True
            opciones = [f"{entrada.name}[{entrada.value}]" for entrada in Entrada]
            opciones_str = ", ".join(opciones)
            seleccion = int(eleccion_jugador)
            entrada = Entrada(seleccion)
            return entrada

#Inicio
# print("""Instrucciones:

# Este es un juego de Piedra, Papel, Tijera, Lagartija, Spock; para la victoria, tienes que ganar 5 rounds!

# Selecciona 
#               '0', para 'piedra, 
#               '1', para 'papel', 
#               '2' para 'tijera', 
#               '3' para 'lagartija', o
#               '4' para 'Spock'
              
#               ¡¡Buena suerte!!
              
#               """)

# def obtener_entrada_jugador():
#     opciones = [f"{entrada.name}[{entrada.value}]" for entrada in Entrada]
#     opciones_str = ", ".join(opciones)
#     seleccion = int(input(f"Elige tu jugada ({opciones_str}): "))
#     entrada = Entrada(seleccion)
#     return entrada

def obtener_entrada_computadora():
    seleccion = random.randint(0, len(Entrada) - 1)
    entrada = Entrada(seleccion)
    return entrada
    
def determinar_ganador(entrada_jugador, entrada_computadora):
    perder = Que_vence_a_que[entrada_jugador]
    if entrada_jugador == entrada_computadora:
        print(f"Ambos eligieron: {entrada_jugador.name}. Empate!")
    elif entrada_computadora in perder:
        print(f"{entrada_jugador.name} le gana a {entrada_computadora.name}! Ganaste!")
        # en "le gana a" insertar metodo choice para elegir caso a caso en diagrama de estrella
    else:
        print(f"{entrada_computadora.name} le gana a {entrada_jugador.name}! Perdiste :v")            

class Continuar(IntEnum):
    Si = 1
    No = 0
    
def jugar_otra_vez():
    opciones = [f"{continuar.name}[{continuar.value}]" for continuar in Continuar]
    opciones_str = ", ".join(opciones)
    seleccion = int(input(f"¿Seguir jugando?\n{opciones_str}"))
    otra_vez = Continuar(seleccion)
    return otra_vez
    
    
while True:
    
    print("""Instrucciones:

    Este es un juego de Piedra, Papel, Tijera, Lagartija, Spock; para la victoria, tienes que ganar 5 rounds!

    Selecciona 
              '0', para 'piedra, 
              '1', para 'papel', 
              '2' para 'tijera', 
              '3' para 'lagartija', o
              '4' para 'Spock'
              
              ¡¡Buena suerte!!
              
              """)
    
#     try:
    entrada_jugador = user()
#     except ValueError as e:
#         range_str = f"[0 y {len(Entrada) - 1}\n]"
#         print(f"Entrada incorrecta. Por favor elige un valor entre {range_str}\n")
#         continue

    entrada_computadora = obtener_entrada_computadora()
    determinar_ganador(entrada_jugador, entrada_computadora)
    
    perder = Que_vence_a_que[entrada_jugador]
    if entrada_jugador == entrada_computadora:
        print(f"Victorias tuyas: {contador_jugador}, Victorias de la computadora {contador_computadora}")
    elif entrada_computadora in perder:
        contador_jugador += 1
        print(f"Victorias tuyas: {contador_jugador}, Victorias de la computadora {contador_computadora}")
    else:
        contador_computadora += 1
        print(f"Victorias tuyas: {contador_jugador}, Victorias de la computadora {contador_computadora}")
   
    try:
        if contador_jugador == 5:
            print(string1)
            break
        elif contador_computadora == 5:
            print(string2)
            break
    except:
        continue

    try:
        seguir = jugar_otra_vez()
    except ValueError as e:
        range_str = f"[0 y 1]"
        print(f"Entrada incorrecta. Por favor elige un valor entre {range_str}")
#     except: # Con este except el código reinicia el juego
    if seguir == 0:
        break
            
#Pendiente:
#Al acumular 3 victorias traer string winner

