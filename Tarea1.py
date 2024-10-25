import numpy as np
import math

#Tarea Brandon Alfonso Aguilera Salinas
def promedio(x):
    resp=[]
    total=int(0)
    for value in x:
        if not math.isnan(value):
            resp.append(value)

    for value in resp:
       total=total+value 
    
    Size=len(resp)

    promedio=total/Size


        
    return promedio

if __name__=='__main__':
    arr1 = np.linspace(1, 10, num=10)
    arr2 = np.linspace(1, 10, num=10)

    arr2[:] = np.nan
    entrada = np.concatenate((arr1, arr2)) 
    np.random.shuffle(entrada)
 
    salida = promedio(entrada)
    print(entrada)
    print(salida)