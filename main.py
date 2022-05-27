import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('https://raw.githubusercontent.com/whitehatjr/bell-curve--normal-distribution/master/data.csv')
list = df ['Avg Rating']
fig = ff.create_distplot([list],['Avg Rating Data'])
fig.show()