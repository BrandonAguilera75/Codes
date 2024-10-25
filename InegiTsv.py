import pandas as pd 
import os 
import csv
from datetime import datetime


if __name__ == "__main__" :
    relativepath= os.path.dirname(__file__)
    path_to_open="TSV/muestra_de_base_comext.tsv"
    full_path=os.path.join(relativepath, path_to_open)

    df=pd.read_csv(full_path, encoding="utf8", delimiter="\t")

    print(df)