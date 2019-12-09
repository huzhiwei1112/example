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

ind = np.linspace(0, 2,10)
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(ind,gdp)
ax.set_title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})
ax.set_xticklabels(labels)
plt.grid(True)
plt.show()
