import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data1 = pd.read_csv('day4.csv',encoding='utf8')
data2 = pd.read_csv('per_hour_day3.csv',encoding='utf8')

day4=data1['0'].tolist()
per_hour_day3=data2['0'].tolist()

ee_year=[]
battery=0
while battery<15001:
    rate=0
    while rate<1.01:
        i=0
        ee = []
        eee = []
        while i<8760:
            if i==0:
                ee.append(0)
                eee.append(per_hour_day3[0])
            else:
                if ee[i-1]+day4[i]*rate-per_hour_day3[i]>0:
                    eee.append(0)
                    if ee[i-1]+day4[i]*rate-per_hour_day3[i]>battery:
                        ee.append(battery)
                    else:
                        ee.append(ee[i-1]+day4[i]*rate-per_hour_day3[i])
                else:
                    ee.append(0)
                    eee.append(per_hour_day3[i]-ee[i-1]-day4[i]*rate)

                # if ee[i-1]>0:
                #     if per_hour_day3[i]<day4[i]*rate:
                #         if day4[i]*rate-per_hour_day3[i]+ee[i-1]>battery:
                #             ee.append(battery)
                #         else:
                #             ee.append(day4[i]*rate-per_hour_day3[i]+ee[i-1])
                #     elif ee[i-1]>per_hour_day3[i]:
                #         if ee[i-1]+day4[i]*rate-per_hour_day3[i]>battery:
                #             ee.append(battery)
                #         else:
                #             ee.append(ee[i-1]+day4[i]*rate-per_hour_day3[i])
                #     elif per_hour_day3[i]-day4[i]*rate-ee[i-1]<0:
                #         ee.append(0)
                #     elif per_hour_day3[i]-day4[i]*rate-ee[i-1]>0:
                #
                #         if ee[i-1]>per_hour_day3[i]:
                #             ee.append(ee[i-1]-per_hour_day3[i])
                #         else:
                #             ee.append(0)
                # else:
                #     if per_hour_day3[i]<day4[i]*rate:
                #         ee.append(day4[i]*rate-per_hour_day3[i])
                #     else:
                #         ee.append(0)

            i=i+1

        ee_year.append(sum(eee))
        rate=rate+0.01

    battery=battery+100
    # print(battery)

ee1=np.array(ee_year).reshape(151,101)/100



file=pd.DataFrame(data=ee1)
file.to_csv('heatmap.csv')
