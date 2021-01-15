import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("FEH_00200524_210115184544.csv", index_col="全国・都道府県", encoding="shift_jis")
# print(len(df))
# print(df.columns.values)

df = df.drop("全国", axis=0)

# データをグラフ化する
df["2019年"]  = pd.to_numeric(df["2019年"].str.replace(",", "")) #数字のカンマを削除
df["2018年"]  = pd.to_numeric(df["2018年"].str.replace(",", "")) #数字のカンマを削除
df["人口増減"] = df["2019年"] - df["2018年"]
df = df.sort_values("人口増減", ascending=False)
df["人口増減"].plot.bar(figsize=(10, 6))
plt.ylim(-40, 14000)
plt.show()