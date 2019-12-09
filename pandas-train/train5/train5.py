import pandas as pd


raw_data1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}

raw_data2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}

raw_data3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}

# 1.自定义数据框
data1 = pd.DataFrame(raw_data1,columns=['subject_id','first_name','last_name'])
data2 = pd.DataFrame(raw_data2,columns=['subject_id','first_name','last_name'])
data3 = pd.DataFrame(raw_data3,columns=['subject_id','test_id'])
print(data1)
print(data2)
print(data3)

# 2.将data1和data2按照行维度进行合并和按照列的维度进行合并
# 按行合并
data_12_row = pd.concat([data1,data2])
print(data_12_row)
# 按列合并
data_12_col = pd.concat([data1,data2],axis=1)
print(data_12_col)
# 按指定行合并
print(pd.merge(data1, data2, on='subject_id', how='inner')) # join
print(pd.merge(data1, data2, on='subject_id', how='left')) # left join
print(pd.merge(data1, data2, on='subject_id', how='right')) # right join
print(pd.merge(data_12_row,data3,on='subject_id')) # 默认是inner join
print(pd.merge(data_12_row,data3,on='subject_id',how='inner'))
print(pd.merge(data1, data2, on='subject_id', how='outer'))

