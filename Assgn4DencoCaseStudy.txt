
import pandas as pd
df = pd.read_csv('data/denco.csv')
loyal = df.groupby("custname").count()
sol1 = loyal.sort_values('region',ascending=[0])
sol1.head(5)
revenue = df.groupby("custname").sum()
sol2 = revenue.sort_values('revenue',ascending=[0])
sol2.head(5)
partRevenue = df.groupby("partnum").sum()
sol3 = partRevenue.sort_values('revenue',ascending=[0])
sol3.head(5)
sol4 = partRevenue.sort_values('margin',ascending=[0])
sol4.head(5)
