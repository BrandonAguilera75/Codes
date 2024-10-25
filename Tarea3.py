#Aguilera Salinas Brandon Alfonso
from PIL import Image, ImageOps
from matplotlib import pyplot as plt
import numpy as np
import os

if __name__ =="__main__":
    absolute_path=os.path.dirname(__file__)
    relative_path="colors.jpg"
    full_path=os.path.join(absolute_path,relative_path)
    
    x=128
    y=128

    
    img=Image.open(full_path)
    imgRGB=img.resize((128,128),resample=Image.Resampling.BICUBIC)
    imgHSV=imgRGB.convert("HSV")
    
    data=np.array(imgHSV)
    color_rgb=np.array(imgRGB)

     
    hue=data[:,:,0]
    hue=hue/255 *359

    sat=data[:,:,1]
    sat=sat/255 * 100 

    target_hues = [227, 0, 120]

    for tarhue in target_hues:
        hue_mask = np.logical_and(np.abs(hue - tarhue) < 40, sat > 30)
        
        # Hacer una copia del array de datos original
        modified_data = np.copy(data)
        
        # Ajustar la saturación a 0 en toda la imagen
        modified_data[:, :, 1] = 0
        
        # Ajustar el valor (brillo) a 0 en las áreas que cumplen la condición
        modified_data[hue_mask, 2] = 0

        # Convertir de nuevo a imagen PIL HSV
        imgHSV_mod = Image.fromarray(modified_data, 'HSV')
        
        # Convertir de HSV a RGB
        imgRGB_mod = imgHSV_mod.convert("RGB")

        plt.imshow(imgRGB_mod)
        plt.show()


