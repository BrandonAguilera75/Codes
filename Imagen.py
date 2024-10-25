from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os

if __name__ =="__main__":
    absolute_path=os.path.dirname(__file__)
    relative_path="imagenes"
    full_path=os.path.join(absolute_path,relative_path)

    x=128
    y=128
    for file in os.listdir(full_path):
        if file.endswith(".jpg"):
            img_path=os.path.join(full_path, file)
            img=Image.open(img_path)
            
            imgRGB=img.resize((128,128),resample=Image.Resampling.BICUBIC)
            imgHSV=imgRGB.convert("HSV")

            data=np.array(imgHSV)
            C=np.array(imgRGB)
            R=C[:,:,0]
            G=C[:,:,1]
            B=C[:,:,2]
            
            color_math=[]
            for i in range(x):
                for j in range(y):
                    color_math.append((R[i,j]/255, G[i,j]/255, B[i,j]/255))
            
            color_math=np.array(color_math)

            fig=plt.figure(figsize=(10,7))
            ax=plt.axes(projection="3d")
            plt.scatter(data[:,:,0],data[:,:,1],data[:,:,2], c=color_math)
            
            plt.show()

        