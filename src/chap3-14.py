import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

col = ["国語","数学","英語"]
idx =  ["A太","B介","C子","D郎","E美", "F菜"]
data =  [
    [83,89,76],
    [66,93,75],
    [100,84,96],
    [60,73,40],
    [92,62,84],
    [96,92,95],
]
df = pd.DataFrame(data, columns=col, index=idx)
df.to_csv("test.csv")

# print(df)

# 全体の表示
# df.plot.bar()
# plt.legend(loc="lower right")
# plt.show()

# df.plot.barh()
# plt.legend(loc="lower right")
# plt.show()

# df.plot.bar(stacked=True)
# plt.legend(loc="lower right")
# plt.show()

# df.plot.box()
# plt.show()

# df.plot.area()
# plt.legend(loc="lower right")
# plt.show()

# 個別の表示 
# df["国語"].plot.barh()
# plt.legend(loc="lower left")
# plt.show()

# df.loc["C子"].plot.barh()
# plt.legend(loc="lower left")
# plt.show()

# df.loc["C子"].plot.pie(labeldistance=0.6)
# plt.legend(loc="lower left")
# plt.show()

df.T.plot.bar()
plt.legend(loc="lower right")
plt.show()

# fig の保存
plt.savefig("bargraph.png")