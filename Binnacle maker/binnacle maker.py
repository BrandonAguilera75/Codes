import pandas as pd 
import os 
import csv
from spire.doc import *
from spire.doc.common import *
import docx
import tkinter
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import math
from openpyxl import Workbook
import numpy as np

global df_bd

df_bd =pd.read_excel('CONTROL RUT200.xlsx')


def maxLength(col):
    max_length = -math.inf
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    return (max_length + 2)

def ruta():
    archivo = askopenfilename(
        filetypes=[("Archivos de Excel", "*.xlsx *.xls")]
    )
    if archivo:
        # Hacemos la comparación sin el espacio final y en minúsculas
        if "consumos" in os.path.basename(archivo).lower():  # Se eliminó el espacio y se busca solo "consumos"
            global df_consumos
            df_consumos = pd.read_excel(archivo)
            messagebox.showinfo("Archivo Seleccionado", "Archivo cargado correctamente.")
        else:
            noarch = Tk()
            noarch.geometry("400x100")
            noarch.title("Advertencia")
            noarchlabel = tkinter.Label(noarch, text="El archivo seleccionado no cumple con el formato esperado.")
            noarchlabel.grid(row=0, column=0)
            noarch.mainloop()  # Asegurarse de mostrar la ventana emergente
    else:
        noarch = Tk()
        noarch.geometry("400x100")
        noarch.title("Advertencia")
        noarchlabel = tkinter.Label(noarch, text="No se seleccionó ningún archivo")
        noarchlabel.grid(row=0, column=0)
        noarch.mainloop()  # Asegurarse de mostrar la ventana emergente)



def CreateBinnacle():
    
    df_bd["IDENTIFICADOR"] = df_bd["IDENTIFICADOR"].str.strip()
    df_bd["CONCESIONARIO"] = df_bd["CONCESIONARIO"].str.strip()
    Identificador=df_bd["IDENTIFICADOR"]
    Consecion=df_bd["CONCESIONARIO"]
    Equipos = df_consumos["EQUIPOS A REVISAR"].str.strip()

    global  lista_dinamica
    lista_dinamica={}
   
    for elem in Equipos:
        if len(str(elem)) == 0:
            del Equipos[elem]
    
    for i in Equipos:
        for j in Identificador:
         if Equipos[i] == Identificador[j]:
             con_act = Consecion[j] 
             if con_act == ("" or Consecion[j-1]):
              lista_dinamica[f"Concesion_{con_act}"].append(Equipos[i])
             else:
               con_act = Consecion[j] 
               lista_dinamica[f"Concesion_{con_act}"].append(Equipos[i])
            



    



           


if __name__ == "__main__":
    pantalla = Tk()
    pantalla.geometry("500x200")
    pantalla.title("Binnacle Maker")

    texto = tkinter.Label(pantalla, text="Seleccione su Archivo")
    texto.grid(row=0, column=0)
    OpArch = tkinter.Button(pantalla, text="Examinar Archivos", command=ruta) 
    OpArch.grid(row=0, column=1)

    
    savename = tkinter.Button(pantalla, text="Crear Bitacoras", command=CreateBinnacle)
    savename.grid(row=1, column=3)
    pantalla.mainloop()
    print(lista_dinamica)
