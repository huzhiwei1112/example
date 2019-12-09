import pandas as pd

drinks = pd.read_csv('drinks.csv',sep=',')
print(drinks.head())

# 1.计算每个大陆平均消耗的啤酒
print(drinks.groupby('continent').beer_servings.mean())

# 2.展示每个大陆的红酒消耗的描述性统计值
print(drinks.groupby('continent').wine_servings.describe())

# 3.展示每个大陆每种酒类的消耗平均值
print(drinks.groupby('continent').mean())

# 4.展示每个大陆每种酒类别的消耗中位数
print(drinks.groupby('continent').median())

# 5.展示每个大陆对spirit饮品消耗的平均值，最大值和最小值
print(drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'std', 'count']))