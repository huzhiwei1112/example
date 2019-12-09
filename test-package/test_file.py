import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn import datasets,linear_model
from sklearn.linear_model import LogisticRegression

date_list = []
sale_list = []
begin = datetime.date(2019,1,1)
end = datetime.date(2019,10,16)
for i in range((end-begin).days+1):
    day = begin+datetime.timedelta(days=i)
    date_list.append(str(day))
    sales = random.randint(1,100)
    sale_list.append(sales)
tick_spacing = 72
fig, ax = plt.subplots(1,1)
ax.plot(date_list,sale_list)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()

regr = linear_model.LinearRegression()
f = ['']
regr.fit(date_list,sale_list)
predict_result = regr.predict('2019-11-02')
print(predict_result)


