import pandas as pd
import tkinter
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import os 
import math
from openpyxl import Workbook
import numpy as np

df = None

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
    global df
    
    archivo = askopenfilename(
        filetypes=[("Archivos de Excel", "*.xlsx *.xls")]
    )
    if archivo:
        if "reporte-sitek" in os.path.basename(archivo).lower():
            df = pd.read_excel(archivo)
        else:
            noarch = Tk()
            noarch.geometry("400x100")   
            noarch.title("Advertencia")
            noarchlabel = tkinter.Label(noarch, text="El archivo seleccionado no cumple con el formato esperado.")
            noarchlabel.grid(row=0, column=0)
    else:
        noarch = Tk()
        noarch.geometry("400x100")   
        noarch.title("Advertencia")
        noarchlabel = tkinter.Label(noarch, text="No se seleccionó ningún archivo")
        noarchlabel.grid(row=0, column=0)

def getname():
    global df
    newname = nombre.get()

    if df is not None:

        if newname == "":
            messagebox.showwarning("Advertencia", "No es posible usar caracteres especiales, espacios o nombres vacíos")
        else:
            namearch = newname

            # Eliminar espacios en blanco al principio y al final
            df["NOMBRE EQUIPO"] = df["NOMBRE EQUIPO"].str.strip()

            # Filtrar por nombres que contienen "URB"
            df_filtrado = df[df["NOMBRE EQUIPO"].str.contains("URB", case=False, na=False)].copy()
            
            df_filtrado["Consumo del dia anterior"] = pd.to_numeric(df_filtrado["Consumo del dia anterior"], errors='coerce')

            # Filtrar los equipos con consumo menor a 10
            nombres_equipos_cero = df_filtrado.loc[df["Consumo del dia anterior"] < 10, "NOMBRE EQUIPO"]
            df_filtrado["Nombres equipos consumo cero"] = nombres_equipos_cero.str.extract('(\d+)')

            lista_elem=nombres_equipos_cero.tolist()
            
            for elem in lista_elem:
                if len(str(elem)) == 0:
                 del lista_elem[elem]

            lista_extendida = lista_elem + [np.nan] * (len(df_filtrado) - len(lista_elem))
            


            df_filtrado["Nombres equipos consumo cero"]=lista_extendida

            # Extraer solo los números de los nombres de equipo
            
            
            

            wb = Workbook()
            ws = wb.active
            
            # Definir los encabezados específicos
            headers = ["MSISDN", "CLIENTE", "NOMBRE EQUIPO", "Inicio 6AM", 
                       "Incremento en el transcurso del dia", "Fin 12PM", 
                       "Consumo del dia anterior", "MB actuales", "Nombres equipos consumo cero"]
            
            # Agregar encabezados al inicio del archivo
            ws.append(headers)
            
            # Añadir los datos filtrados al nuevo archivo de Excel
            lista = df_filtrado.values.tolist()
            for row in lista: 
                ws.append([cell if pd.notna(cell) else "" for cell in row])
            
            # Ajustar ancho de columnas
            for col in ws.columns:
                max_length = maxLength(col)
                column = col[0].column_letter 
                ws.column_dimensions[column].width = max_length
            
            # Guardar el archivo en el escritorio
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            try:
                wb.save(os.path.join(desktop_path, namearch + ".xlsx"))
                messagebox.showinfo("Guardado", "Archivo guardado correctamente en el escritorio")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
    else:
        messagebox.showwarning("Advertencia", "No se ha cargado ningún archivo")

if __name__ == "__main__":
    pantalla = Tk()
    pantalla.geometry("500x200")
    pantalla.title("Archivos de Excel")

    texto = tkinter.Label(pantalla, text="Seleccione su Archivo")
    texto.grid(row=0, column=0)
    OpArch = tkinter.Button(pantalla, text="Examinar Archivos", command=ruta) 
    OpArch.grid(row=0, column=1)

    texto2 = tkinter.Label(pantalla, text="Seleccione el Nombre para su archivo")
    texto2.grid(row=1, column=0)
    nombre = tkinter.Entry(pantalla)
    nombre.grid(row=1, column=1)
    savename = tkinter.Button(pantalla, text="Guardar Archivo", command=getname)
    savename.grid(row=1, column=3)

    pantalla.mainloop()