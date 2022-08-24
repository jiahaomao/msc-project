import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import MultipleLocator
import csv
import pandas as pd
from price import bp,sp

need_year_1 = pd.read_csv('heatmap2.csv',encoding='utf8')
# need_year=np.array(need_year_1)
# need_year_2=[need_year[i:i+131] for i in range (0,len(need_year), 131)]
# sadasd

# x=[1,2,3,4,5]
# y=[2,3,4,5,6]
# m=[[1],[2],[3]]
# x1=np.array(x)
# y1=np.array(y)
# y2=y1.reshape(y1.shape[0],1)
# m1=np.array(m)
# print(x1,y1)
# z=x1*y2
# n=x1*m1
# asdasdasd


x = np.arange(0,101)
y = np.arange(0,151)
m = np.arange(0,101)
n = np.arange(0,151)
o = np.arange(0,101)
p = np.arange(0,151)
z = np.array(need_year_1)

electricity_price=z*48.34*20*(1+0.01+0.01**2+0.01**3+0.01**4+0.01**5+0.01**6+0.01**7+0.01**8+0.01**9+0.01**10+0.01*11+0.01**12+0.01**13+0.01**14+0.01**15+0.01**16+0.01**17+0.01**18+0.01**19)*(1+0.02+0.02**2+0.02**3+0.02**4+0.02**5+0.02**6+0.02**7+0.02**8+0.02**9+0.02+0.02**2+0.02**3+0.02**4+0.02**5+0.02**6+0.02**7+0.02**8+0.02**9)
#   #1
solarpanel_price=(sp[0]*(m*40)**2+sp[1]*(m*40))/2000
battery_price=(bp[0]*(n/10)**3+bp[1]*(n/10)**2+bp[2]*(n/10))*2

cost=solarpanel_price*battery_price.reshape(battery_price.shape[0],1)/1000+electricity_price/1000

# 45.7% CCGT 4.4% Oil,gas 10.2% Coal
# ccc=(0.457*350000/10000000000+0.44*0.08+0.102*997/1000)
# CO2_emission = z*ccc




fig, ax = plt.subplots()
im = ax.imshow(z)
# fig2, ax2 = plt.subplots()
# im2 = ax2.imshow(cost)

ax.set_xticks(np.arange(len(x)))
ax.set_yticks(np.arange(len(y)))

ax.set_xticklabels(x)
ax.set_yticklabels(y)

# ax2.set_xticks(np.arange(len(m)))
# ax2.set_yticks(np.arange(len(n)))
#
# ax2.set_xticklabels(m)
# ax2.set_yticklabels(n)

# for i in range(len(x)):
#     for j in range(len(y)):
#         text = ax.text(j, i, harvest[i, j], color="w")

fig.tight_layout()
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
plt.ylabel('Solar panel power generation efficiency (%)')
plt.xlabel('Energy storage battery capacity (100Wh)')
plt.colorbar(im)

# fig2.tight_layout()
# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
# plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
# plt.ylabel('%')
# plt.xlabel('100Wh')
# plt.colorbar(im2)

fig=plt.figure()
ax=Axes3D(fig)
x,y=np.meshgrid(x,y)
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap='rainbow')
ax.set_ylabel('Energy storage battery capacity (100Wh)')
ax.set_xlabel('Solar panel power generation efficiency (%)')
ax.set_zlabel('additional power required (W)')



fig2=plt.figure()
ax2=Axes3D(fig2)
m,n=np.meshgrid(m,n)
ax2.plot_surface(m,n,cost,rstride=1,cstride=1,cmap='rainbow')
ax2.set_ylabel('Energy storage battery capacity (100Wh)')
ax2.set_xlabel('Solar panel power generation efficiency (%)')
ax2.set_zlabel('System cost (£)')

# fig3=plt.figure()
# ax3=Axes3D(fig3)
# o,p=np.meshgrid(o,p)
# ax3.plot_surface(o,p,CO2_emission,rstride=1,cstride=1,cmap='rainbow')
# ax3.set_ylabel('100Wh')
# ax3.set_xlabel('%')
# ax3.set_zlabel('g')

plt.show()
