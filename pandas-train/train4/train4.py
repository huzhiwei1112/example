import numpy as np
import pandas as pd

crime = pd.read_csv('US_Crime_Rates_1960_2014.csv',sep=',')
print(crime.head())
print(crime.info())

# 1.将年份的数据类型从int64改为datetime64
crime.Year = pd.to_datetime(crime.Year,format='%Y')
print(crime.info())

# 2.将Year设置为数据框的索引
crime = crime.set_index('Year',drop=True)
print(crime.head())
# 3.删除row_num列
del crime['row_num']
del crime['Total']
print(crime.head())

# 4.对每个世纪的数据进行汇总，也就是没10行进行统计，前提是数据根据年份排序过了
crimes = crime.resample('10AS').sum()
crimes['Population'] = crime['Population'].resample('10AS').max()
print(crimes)

# 5.获取每一列的最大值
print(crime.idxmax(0))
