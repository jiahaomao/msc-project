import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d
import csv
import pandas as pd
from sklearn.linear_model import Ridge
import regressors.stats


file = pd.read_csv('price.csv',encoding='utf8')
battery_x= file['KWh'].tolist()
del battery_x[45:121]
battery_y= file['price1'].tolist()
del battery_y[45:121]
solarpanel_x= file['W'].tolist()

solarpanel_y= file['price2'].tolist()


# clf=Ridge(alpha=1.0)
# clf.fit(solarpanel_x,solarpanel_y)
#
# print(clf.score(solarpanel_x,solarpanel_y))
# print(clf.coef_)
# print(clf.get_params())

# bp=np.polyfit(battery_x,battery_y,2)
# battery_polyfit=bp[0]*np.array(battery_x)**2+bp[1]*np.array(battery_x)+bp[2]

# bp=np.polyfit(battery_x,battery_y,1)
# battery_polyfit=bp[0]*np.array(battery_x)+bp[1]

bp=np.polyfit(battery_x,battery_y,3)
battery_polyfit=bp[0]*np.array(battery_x)**3+bp[1]*np.array(battery_x)**2+bp[2]*np.array(battery_x)


# bp=np.polyfit(battery_x,battery_y,4)
# battery_polyfit=bp[0]*np.array(battery_x)**4+bp[1]*np.array(battery_x)**3+bp[2]*np.array(battery_x)**2+bp[3]*np.array(battery_x)

sp=np.polyfit(solarpanel_x,solarpanel_y,1)
solarpanel_polyfit=sp[0]*np.array(solarpanel_x)+sp[1]




# plt.figure(1)
# plt.scatter(battery_x,battery_y)
# plt.plot(battery_x,battery_polyfit,'r',label='y=%s*x^3+%s*x^2+%s*x' % ("{0:.4}".format(bp[0]),"{0:.4}".format(bp[1]),"{0:.4}".format(bp[2])))
# plt.legend()
#
# plt.figure(2)
# plt.scatter(solarpanel_x,solarpanel_y)
# plt.plot(solarpanel_x,solarpanel_polyfit,'r',label='y=%s*x' % ("{0:.4}".format(sp[0])))
# plt.legend()
# plt.show()

# sp=np.polyfit(solarpanel_x,solarpanel_y,2)
# solarpanel_polyfit=sp[0]*np.array(solarpanel_x)**2+sp[1]*np.array(solarpanel_x)


