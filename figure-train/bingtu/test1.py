import numpy as np
import matplotlib.pyplot as plt

labels = [
    'USA', 'China', 'India',
    'Japan', 'Germany', 'Russia',
    'Brazil', 'UK', 'France', 'Italy'
]
gdp = [
    15094025.0, 11299967.0, 4457784.0,
    4440376.0, 3099080.0, 2383402.0,
    2293954.0, 2260803.0, 2217900.0, 1846950.0
]
plt.figure(1, figsize=(6,6))
expl = [0,0.1,0,0,0,0,0,0,0,0]
colors  = ["blue","red","coral","green","yellow","orange"]
plt.pie(gdp, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)
plt.title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})
plt.show()