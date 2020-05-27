# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:02:28 2019
@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd #Se importa la libreria PANDAS
import numpy as np #Se importa la librerias NUMPY

"""Se lee el archivo de Excel como un DataFrame usando libreria Pandas"""
EFelicidad = pd.read_excel('Final_Felicidad_Dicotomizadas(7_11_2019).xlsx',
                           sheet_name='Respuestas de formulario 1').drop(['Marca temporal',
                                                                          'Dirección de correo electrónico'], axis=1)

"""Se reemplaza de acuerdo a la elección tomada de 1 a 5 con 
                   las opcciones respectivas desde Totalmente en desacuerdo a Totalmente de acuerto"""
EFelicidad = EFelicidad.replace(["Totalmente en desacuerdo", "Algo en desacuerdo",
                                 "Ni en acuerdo ni desacuerdo", "Algo de acuerdo",
                                 "Totalmente de acuerdo"],
                                [1, 2, 3, 4, 5])


def invertirColumnas(matriz):  # Inicio método invertirColumnas paso parámetro matriz
    matrizEfelicidadPD = pd.DataFrame(matriz).copy()  # Se crea una copia del DataFrame matriz
    for i in range(len(matriz)):  # Inicio del condicional
        # recorriendo el numero de items de la matriz
        if i == 0 or i == 4 or i == 5 or i == 9 or i == 12 or i == 13 or i == 18 or i == 22 or i == 23 or i == 26 or i == 27 or i == 28:
            # if corre[i]<0:
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 1, i] = -5
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 2, i] = -4
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 4, i] = 2
            matrizEfelicidadPD.loc[matrizEfelicidadPD[i] == 5, i] = 1
    matrizEfelicidadPD = abs(matrizEfelicidadPD)  # Devuelve el valor absoluto de matrizEfelicidadPD
    return matrizEfelicidadPD.to_numpy()  # Regresa matrizEfelicidadPD como un array de NumPY(ndarray)


def generarClase(vector, med):  # Inicio método generarClase parámetros vector, med
    salida = []  # Crea un vector vacio llamado salida
    for x in vector:
        if (x < med):
            salida.append(0)  # Agrega 0 al vector salida
        else:
            salida.append(1)  # Agrega 1 al vector salida
    return salida


EFelicidadCSV = EFelicidad.to_numpy()
creaTablaNumericarCSV = invertirColumnas(EFelicidadCSV)
EFelicidadcsv = creaTablaNumericarCSV
EFelicidadcsv2 = EFelicidadcsv[:, 0:29]
sumaMuestras = EFelicidadcsv2.sum(axis=1) / 29
media = sumaMuestras.mean()
claseGenerada = np.array(generarClase(sumaMuestras.copy(), media))
crearCSVEF = pd.DataFrame(creaTablaNumericarCSV, columns=EFelicidad.columns)
crearCSVEF['clase'] = claseGenerada.reshape(len(claseGenerada), 1)
# np.hstack((EFelicidadcsv,claseGenerada.reshape(len(claseGenerada),1)))
# lo anterior agrega una columan en numpy
# 'tablaCon29REguntasInvertidas.csv', mode='a', index=False, header=False,sep=';',decimal=','
crearCSVEF.to_csv('DFnumericoInvertido.csv', index=False, sep=',')

# Encuesta FELICIDAD- Factor_ Personal (respuestas)
Epersonal = pd.read_excel('Encuesta FELICIDAD- Factor_ Personal (respuestas).xlsx',
                          sheet_name='Respuestas de formulario 1').drop(['Marca temporal',
                                                                         'Dirección de correo electrónico: '], axis=1)

Epersonal = Epersonal.replace(['No', 'Si', 'Sí'], [0, 1, 1])
Epersonal = Epersonal.replace(['Masculino', 'Femenino'], [1, 0])
Epersonal = Epersonal.replace(['Facultad de Ciencias y Educación'], [0])
Epersonal = Epersonal.replace(['Facultad de Ingeniería'], [1])
Epersonal = Epersonal.replace(['Facultad de Medio Ambiente y Recursos Naturales'], [2])
Epersonal = Epersonal.replace(['Facultad Tecnológica'], [3])
Epersonal = Epersonal.replace(['Facultad de Artes - ASAB'], [4])
Epersonal = Epersonal.replace(['Soltero', 'Otro'], [0, 1])
Epersonal = Epersonal.replace(['LA REGIÓN CARIBE.', 'LA REGIÓN ANDINA.'], [0, 1])
Epersonal = Epersonal.replace(['LA REGIÓN PACÍFICA.', 'LA REGIÓN AMAZÓNICA.'], [2, 3])
Epersonal = Epersonal.replace(['LA REGIÓN DE LOS LLANOS ORIENTALES.', 'LA REGIÓN INSULAR.'], [4, 5])
Epersonal = Epersonal.replace(['Introvertido', 'Extrovertido', 'Histérico', 'Ansioso-obsesivos.', 'Ansioso-obsesivo'],
                              [0, 1, 2, 4, 4])
Epersonal = Epersonal.replace(['60 minutos o menos', 'más de 60 minutos'], [0, 1])
Epersonal.to_csv('EPnumerio.csv', index=False, sep=',')
