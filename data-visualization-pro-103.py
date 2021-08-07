import pandas as pd
import plotly.express as px

data = pd.read_csv('C:/Users/Admin/OneDrive/Desktop/Python/Pro-103/Data-visualization-master/csv files/covidData.csv')
fig = px.scatter(data,x="date",y="cases",color="country",title="Covid 19 Cases in world", size ="cases")
fig.show()