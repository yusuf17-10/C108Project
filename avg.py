import csv 
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px

data=pd.read_csv("data.csv")

fig =ff.create_distplot([data["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)

fig.show()