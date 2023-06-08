import pandas as pd
import plotly.express as px

df_fa = pd.read_csv('data_science/data/fa_clean_1.csv')
df_fa = df_fa[~(df_fa['Unit'] == 'Litres per person, per year')]

df_fa = df_fa.set_index('Year', drop=True)
df_fa = df_fa.groupby(df_fa.index).sum(numeric_only=True)

fig = px.line(df_fa, x=df_fa.index, y=['Value'],
              title='Food available per person', labels={'value': 'kg of food'})
fig.show()
