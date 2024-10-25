import pandas as pd 
import os 
import csv
from datetime import datetime


if __name__ == "__main__" :
    relativepath= os.path.dirname(__file__)
    path_to_open="CSv/conjunto_de_datos/denue_inegi_23_.csv"
    full_path=os.path.join(relativepath, path_to_open)

    df=pd.read_csv(full_path, encoding="Latin-1")
    
    telearr = []
    for elem in df["telefono"]:
        if type(elem) == type ("") and elem.isnumeric():
            telearr.append(elem)
        else:
            telearr.append("0")
    
    for elem in telearr:
        if type(elem) == type ("") and elem.isnumeric():
            continue
        else:
            print("No se limpio")

    df2=pd.DataFrame(telearr).astype("float64")
    df["telefono"]=df2

   

    fechaarr=[]

    for elem in df["fecha_alta"]:
        try:
         datetime.striptime(elem, "%Y-%m")
         fechaarr.append(elem)
        except:
         cleanelem="-".join(elem.split(" "))
         fechaarr.append(cleanelem)
         

    df3=pd.DataFrame(fechaarr)
    df3[0]=pd.to_datetime(df3[0],format="%Y-%m")

    df["fecha_alta"]=df3
    print(df.dtypes)
    