import pandas as pd
###################################################################
# 数据集字段
# order_id	quantity	item_name	choice_description	item_price
# 订单号   商品数 商品名称    选择理由    金额
# 示例数据
# 1	1	Chips and Fresh Tomato Salsa	NULL	$2.39
###################################################################
# 1.导入本地数据集
chipo = pd.read_csv('chipotle.tsv',sep='\t')
# 2.查看前十行
head10_lines = chipo.head(10)
print(head10_lines)
# 查看某一列也可以这样
# print(chipo.item_name)

# 3.查看有多少列
col_cnt = chipo.shape[1]
# print(chipo.shape[0])
print(col_cnt)

# 4.查看列名
col_name_list = chipo.columns
print(col_name_list)

# 5.查看数据集索引
index = chipo.index
print(index)

# 6.查看被下单数最多的商品
# 根据item_name对quantity进行sum
a = chipo[['item_name','quantity']].groupby(['item_name'],as_index=False).agg({'quantity': 'sum'})
# 根据quantity进行降序排序
a.sort_values(['quantity'],ascending=False,inplace=True)
# 可选topN，默认top5
result = a.head() # result = a.head(10) 选top10
print(result)

# 7.item_name这一列总共有多少个商品被下单
item_cnt = chipo['item_name'].nunique()
print(item_cnt)

# 8.在choice_description中，下单次数最多的top5商品
print(chipo['choice_description'].value_counts().head())
# 在item_name中，下单次数最多的top5商品
print(chipo['item_name'].value_counts().head())

# 9.一共有多少商品被下单
total_orders = chipo['quantity'].sum()
print(total_orders)

# 10.将item_price转换成浮点数
dollarizer = lambda x:float(x[1:-1])
chipo['item_price'] = chipo['item_price'].apply(dollarizer)
print(chipo['item_price'])

# 11.算总收入
# 自定义一个sub_total列，计算每笔订单的收入
chipo['sub_total'] = round(chipo['item_price']*chipo['quantity'],2)
print(chipo['sub_total'] )
total_money = chipo['sub_total'].sum()
print(total_money)

# 12.计算总订单数
order_cnt = chipo['order_id'].nunique()
print(order_cnt)

# 13.计算每一单的平均总价
# 根据订单号对金额做group by
order_pay = chipo[['order_id','sub_total']].groupby(by=['order_id'])
print(order_pay['order_id'],order_pay['sub_total'])
avg_pay = order_pay.agg({'sub_total': 'sum'})['sub_total'].mean()
print(avg_pay)


###################################################################
# 总结
# 1.导入数据集：chipo = pd.read_csv('chipotle.tsv',sep='\t')，数据集与此文件在同一目录下，数据集中的分隔符为\t
# 2.抽样查看数据：chipo.head()抽样查看前几行，默认5行，在head(n)中加参数，就是查看头n行
# 3.查看列数：chipo.shape[1]，查看行数：chipo.shape[0]，查看列名列表：chipo.columns
# 4.自定义列：chipo['sub_total'] = round(chipo['item_price']*chipo['quantity'],2)
# 5.将值转换成浮点数的值：chipo['item_price'].apply(lambda x:float(x[1:-1]))
# 6.查看某一列（可聚合）的topN的名称：chipo[['item_name','quantity']].groupby(['item_name'],as_index=False).agg(
# {'quantity': 'sum'}).sort_values(['quantity'],ascending=False,inplace=True)
# 7.查看某一列的去重数：chipo['item_name'].nunique()
# 8.对某一列数值进行汇总：chipo['quantity'].sum()
# 9.根据某一列聚合另外一个值之后求平均值：chipo[['order_id','sub_total']].groupby(by=['order_id']).agg(
# {'sub_total': 'sum'})['sub_total'].mean()
# 10.读取文件的时候设置列名和索引
pd.read_csv('',
            sep='可使用正则',      # 文件中列之间的间隔符号
            header=None,            # 去掉文件中的标题
            names=['','',''],       # 自定义列名
            index_col=['',''],      # 设置索引列，可多列，可一列
            skiprows=[0,3,5],       # 跳过指定行
            na_values=["java","c++"]# 将指定值替换成NaN
            # 将指定列中的指定值替换成NaN
            # dict = {'name':['1','2']}
            # na_values=dict
            )