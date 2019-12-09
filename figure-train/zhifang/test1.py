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
width = 0.4
ind = np.linspace(0.5,9.5,10)
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.bar(ind-width/2, gdp, width, color='green')
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.set_xlabel('Country')
ax.set_ylabel('GDP (Billion US dollar)')
ax.set_title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})
plt.grid(True)
plt.show()
