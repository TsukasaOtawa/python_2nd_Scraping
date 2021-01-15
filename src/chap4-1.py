import pandas as pd

df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")
# print(len(df))
# print(df.columns.values)
# results = df[df[2] == 1730012]
# print(results[[2,6,7,8]])
result = df[df[8].str.contains("四谷")]
print(result[[2,6,7,8]])