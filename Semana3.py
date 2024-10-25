import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

if __name__ == "__main__":
    x= np.linspace(1,10)

    a= np.linspace(1,10)
    b=-a
    c=np.sin(x)
    d=2*x
    e=np.cos(x)
    res=np.corrcoef([a,b,c,d,e])
    print(res)

    plt.imshow(res,vmin=-1, vmax=1)
    plt.colorbar()
    plt.show()

    fig=px.imshow(res, zmax=1, zmin=-1)
    fig.show()
