import plotly.express as px
import numpy as np

if __name__=="__main__":
    df=px.data.gapminder().query("year==2007")
    print(df)

    fig=px.sunburst(df, path=["continent", "country"],
                    values ="pop", color="lifeExp",
                    hover_data=["iso_alpha"],
                    color_continuous_scale='RdBu')
    fig.show()    