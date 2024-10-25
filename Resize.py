from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os

if __name__ =="__main__":
    absolute_path=os.path.dirname(__file__)
    relative_path="1R.png"
    full_path=os.path.join(absolute_path,relative_path)
    img=Image.open(full_path)
    imgRGB=img.resize((1200,1600),resample=Image.Resampling.BICUBIC)

    plt.imshow(imgRGB)
    plt.colorbar()
    plt.show()

    imgRGB.save('1R.png')