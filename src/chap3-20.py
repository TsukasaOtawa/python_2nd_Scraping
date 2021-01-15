import pandas as pd
import openpyxl

df = pd.read_csv("test.csv")
kokugo = df.sort_values("国語", ascending=False)
# kokugo.to_excel("csv_to_excel1.xlsx")

with pd.ExcelWriter("csv_to_excel3.xlsx") as writer:
    df.to_excel(writer, index=False, sheet_name="元データ")
    kokugo.to_excel(writer, index=False, sheet_name="国語でソート")