#PCA_clase
import plotly.express as px
from plotly import graph_objects as go

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import numpy as np

if __name__ == "__main__":
    df= px.data.iris()
    features=['sepal_length', 'sepal_width',
              'petal_length', 'petal_width']
    print(df)

    x=df.loc[:,features].values
    Y=df.loc[:,['species']].values

    x=StandardScaler().fit_transform(x)
    pca=PCA()
    components= pca.fit_transform(x)

    labels={
        str(i):f"{features[i]} ({var:.1f}%)"
        for i, var in enumerate(pca.explained_variance_ratio_ * 100)

    }

    fig= px.scatter_matrix(components,labels=labels,dimensions=range(4),color=df['species'])

    fig.update_traces(diagonal_visible=False)
    fig.update_layout({"xaxis"+str(i+1): dict(range=[-3,3])for i in range(4)})
    fig.update_layout({"yaxis"+str(i+1): dict(range=[-3,3])for i in range(4)})

    fig.show()

    pca=PCA(n_components=2)
    components=pca.fit_transform(x)

    fig=px.scatter(components, x=0, y=0, color=df['species'])
    fig.show()

    pca=PCA(n_components=3)
    components=pca.fit_transform(x)
    loadings=pca.components_.T
    total_var=pca.explained_variance_ratio_.sum() *100

    fig=px.scatter_3d(components,x=0,y=1,z=2, color=df['species'],
                      title=f'Total Explained Variancie: {total_var:.2f}%')
    
    fig.add_trace(
        go.Scatter3d(
            mode='markers',
            x=[0],
            y=[0],
            z=[0],
            marker=dict(
                color='LigthSkyBlue',
                size=20,
                line=dict(
                    
                )
            )
            
        )
    )
    
    fig.show()