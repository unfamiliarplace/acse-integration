import pandas as pd
import plotly.express as px
import csv

df_fa = pd.read_csv('data_science/data/fa_clean_1.csv')
df_fa = df_fa[~(df_fa['Unit'] == 'Litres per person, per year')]

df_fa = df_fa.set_index('Year', drop=True)
df_fa = df_fa.groupby(df_fa.index).sum(numeric_only=True)

chems = ['Fertilizers, mixed', 'Ammonium nitrate, all grades', 'Ammonium phosphate, all grades', 'Ammonium nitrate phosphate, all grades']

good_vs = {c: ([0] * 52) for c in chems}
with open('data_science/data/chem_clean_1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        y, good, _, v = (c.strip() for c in row)
        if good not in chems:
            continue

        y = int(y.split('-')[0])
        good_vs[good][y - 1958] += float(v) if v else 0

df_pc = pd.DataFrame(index=list(range(1958, 1958+52)))

for (good, vs) in good_vs.items():
    s = pd.Series(vs, index=df_pc.index)
    df_pc[good] = s


df_fa = df_fa[(1959 < df_fa.index) & (df_fa.index < 2001)]
df_pc = df_pc[(1959 < df_pc.index) & (df_pc.index < 2001)]


fig = px.line(df_fa, x=df_fa.index, y='Value',
              title='Food available per person', labels={'value': 'kg of food'})
fig.show()

fig2 = px.line(df_pc, x=df_pc.index, y=df_pc.columns,
              title='Chemical production', labels={'value': 'tonnes of chemical'})
fig2.show()
