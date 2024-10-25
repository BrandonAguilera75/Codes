from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os
import cv2

if __name__ == "__main__":
    absolute_path=os.path.dirname(__file__)
    realtive_path="hues.jpg"
    full_path=os.path.join(absolute_path, realtive_path)

    imgRGB=Image.open(full_path)
    imageHSV=imgRGB.convert("HSV")

    data=np.array(imageHSV)
    hue=data[:,:,0]
    hue=hue/255 * 359
    sat=data[:,:,1]
    sat=sat/255 *100

    target_hue=0

    hue=np.logical_and(np.abs(hue-target_hue)< 5, sat>30)

    plt.imshow(hue)
    plt.colorbar()
    plt.show()
