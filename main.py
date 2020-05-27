# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:28:40 2019
@author: (╯°□°)╯︵ ┻━┻
"""

import ArreglarCSV as ac  # Importa el codigo ArreglarCSV y le asigna el nombre ac
import FiabilidadCronbach as fc  # Importa el codigo FiabilidadCronbach y le asigna el nombre fc


class Main:  # Inicio clase Main

    def __init__(self):  # Clase Init
        self.alfaCronbach = 0  # Se instancia alfaCronbach

    def seleccion(self, numero):  # Funcion  selección, se envía parámetro numero

        if numero == 1:  # Inicio de sentencia condicional if
            ac.ArreglarCSV()  # Si es 1 el objeto ac inicia la función ArreglarCSV
        elif numero == 2:  # Opcion 2 del codicional
            fc.FiablidadCronbach()  # Si es 2 el objeto fc inicia la función resultado()
            self.alfaCronbach = fc.FiablidadCronbach().resultado()
            print(self.alfaCronbach)
    # Fin funcion selección


if __name__ == "__main__":  # Condicional iniciado
    print("John Sebastian Martinez Zabala")
    print("Universidad Distrital Francisco Jose de Caldas")
    opcion = 0
    while opcion >= 0:  # Mientras la opción sea 0 o mayor permanece en el ciclo
        Main()
        print('Para crear CSV escriba 1:')
        print('Para calcular alfa de crombach:')
        print('Para salir ponga 0:')
        opcion = int(input('selecciona una opción\n'))  # Recibe la opcion ingresada como entero
        opcion = int(opcion)
        Main().seleccion(opcion)  # Inicia funcion seleccion de acuerdo a opcion seleccionada
        if (opcion == 0):
            opcion = -1  # Sale del ciclo while
