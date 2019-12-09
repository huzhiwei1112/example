import pandas as pd
import datetime as dt

data = pd.read_table('wind.csv',sep='\s+',parse_dates=[[0, 1, 2]])
# parse_dates=[[0, 1, 2]]是将文件中的前三行，也就是年月日合并到一起，成为日期格式
print(data.head())
print(data.columns)
print(data.shape[1])
print(data.shape[0])
# 1.对数据中的年份进行检测并修正
def fix_centry(x):
    year = x.year - 100 if x.year>1989 else x.year
    return dt.date(year,x.month,x.day)

data.Yr_Mo_Dy = data.Yr_Mo_Dy.apply(fix_centry)
print(data.info())
print(data.head())

# 2.这里的year是object类型，转换成datetime类型
data.Yr_Mo_Dy = pd.to_datetime(data.Yr_Mo_Dy)
print(data.info())
# 设置日期为索引
data = data.set_index('Yr_Mo_Dy')
print(data.head())

# 3.查看每列有多少个缺失值
print(data.isnull().sum())
# 查看每列完整值的个数
print(data.shape[0]-data.isnull().sum())

# 对全体数据，计算风速的平均值
print(data.mean(),data.mean().mean())

# 创建一个名为loc_stats的数据框取计算并存储每个location的风速最小值，最大值，平均值和标准差
loc_stats = pd.DataFrame()
print(data.min())