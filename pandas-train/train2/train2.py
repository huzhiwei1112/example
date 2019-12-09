import pandas as pd

euro12 = pd.read_csv('Euro2012.csv',sep=',')
# 1.查看数据集
print(euro12)

# 2.查看列数和行数
print('cols=%d,rows=%d' % (euro12.shape[1], euro12.shape[0]))

# 3.查看列名
print(euro12.columns)

# 4.总共有多少个队伍参赛
print(euro12['Team'].nunique())

# 5.查看数据集信息
print(euro12.info())

# 6.对数据进行不同维度的分析时，最好将需要的几个数据单独存在一个自定义的数据框中
discipline = euro12[['Team','Yellow Cards','Red Cards']]
print(discipline)
print(discipline.sort_values(['Red Cards','Yellow Cards'],ascending=False))
# 计算平均数
print(discipline['Yellow Cards'].mean())
# 选取某一列大于某个值的记录
print(euro12[euro12['Goals']>6])
# 选取某一个列的值等于或like某个值的记录
print(euro12[euro12['Team']=='Denmark'])
print(euro12[euro12.Team.str.startswith('G')])

# 7.选取前n列
print(euro12.iloc[1:9, 2:3])

# 8.查找指定值
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']])

print(euro12.groupby('Team').mean())
