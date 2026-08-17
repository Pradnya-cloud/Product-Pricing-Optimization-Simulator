import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sc=pd.read_csv(ROOT/"data/price_elasticity_scenarios.csv")
print("Max customers:", int(sc.loc[sc.Customers.idxmax(),"Price"]))
print("Max revenue:", int(sc.loc[sc.Revenue.idxmax(),"Price"]))
print("Max profit:", int(sc.loc[sc.Profit.idxmax(),"Price"]))
print("Max margin:", int(sc.loc[sc["Gross Margin %"].idxmax(),"Price"]))
