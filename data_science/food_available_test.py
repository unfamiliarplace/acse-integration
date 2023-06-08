import pandas as pd
import plotly.express as px

df_fa = pd.read_csv('data_science/data/fa_clean_1.csv')
df_fa = df_fa[~(df_fa['Unit'] == 'Litres per person, per year')]

df_fa = df_fa.set_index('Year', drop=True)
df_fa = df_fa.groupby(df_fa.index).sum(numeric_only=True)

df_pc = pd.read_csv('data_science/data/chem_clean_1.csv')
chems = ['Fertilizers, mixed', 'Ammonium nitrate, all grades', 'Ammonium phosphate, all grades', 'Ammonium nitrate phosphate, all grades']
df_pc = df_pc[df_pc['Good'].isin(chems)].drop('Scale', axis=1)
df_pc['Date'] = df_pc['Date'].map(lambda v: v[:4])

df_pc.set_index(['Date', 'Good'], inplace=True)
df_pc = df_pc.groupby(level=[0, 1]).sum(numeric_only=True)

df_pc = df_pc.reset_index()
df_pc.set_index('Date', inplace=True)

df_pc2 = pd.DataFrame(index=df_pc.index.get_level_values('Date').unique())

for year in df_pc2.index:
    print(df_pc2.loc[year])
    continue
    print(year)
    print()
    for yr_row in df_pc.loc[year]:
        print(yr_row)
    print()
exit()


for chem in chems:
    for year in df_pc2.index:
        yr_row = df_pc.loc[year]
        df_pc2[chem] = df_pc.loc[year].get(chem, pd.NA)

print(df_pc2)

#for year in df_pc.index.unique():
    

#print(df_pc)

# fig = px.line(df_fa, x=df_fa.index, y=['Good', 'Value'],
#               title='Food available per person', labels={'value': 'kg of food'})

#fig.show()

# fig2 = px.line(df_pc, x=df_pc.index, y='Value',
#               title='Chemical production', labels={'value': 'tonnes of chemical'})

# fig2.show()
