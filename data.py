from house_class import house
from renewable_energy import day,day1,day2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

consumption=[]
generation=[]
extra_electricity=[]
lack_electricity=[]
battery_electricity=[]
per_hour_day=[]
a=0
while a<365:


    house_total = house(a)
    house_total.get_power_over_day()
    t_c, val_c = house_total.get_power_over_day()


    # source_total = solar(a)
    # source_total.get_power_over_day_solar_panel()
    # t_g, val_g = source_total.get_power_over_day_solar_panel()

    for i in range(0, 1):
        house1 = house(a)
        house1.tv_power = 130
        house1.printer_power = 1.5
        house1.wireless_power = 10
        house1.phone_charge_power = 10
        house1.electric_fan_power = 50*2
        house1.cooker_hood_power = 200
        house1.extractor_fan_power = 30
        house1.hob_ring_power = 1500
        house1.oven_power = 1500
        house1.microwave_power = 800
        house1.toaster_power = 800
        house1.coffee_maker_power = 1000
        house1.kettle_power = 1500
        house1.lamp_power = 30*10
        house1.desk_lamp_power = 30*5
        house1.desktop_power = 150
        house1.laptop_power = 80
        house1.refrigerator_power = 130
        house1.dishwasher_power = 1500
        house1.washing_power = 70
        house1.tumble_dryer_power = 1500
        house1.hair_dryer_power = 1500
        house1.hoover_power = 500
        house1.get_power_over_day()
        house_total = house_total + house1

    # for i in range(0,1):
    #     source1 = solar(a)e
    #     source1.solar_panel_power=3000
    #     source1.get_power_over_day_solar_panel()
    #     source_tot =source_total + source1


    consumption.append(sum(house_total.ret_val))
    generation.append(day[a]*30)
    per_hour_day.append(house_total.ret_val)
    # per_hour_day.append(house_total.per_hour)
    a=a+1

per_hour_day1=[]
for m in per_hour_day:
    for n in m:
        per_hour_day1.append(n)

per_hour_day2=np.array(per_hour_day1)/100
day3=np.array(day2)/100*30

per_hour_day3=per_hour_day2.reshape(-1,100).sum(1)
day4=day3.reshape(-1,100).sum(1)


file1=pd.DataFrame(data=day4)
file1.to_csv('day4.csv')

file2=pd.DataFrame(data=per_hour_day3)
file2.to_csv('per_hour_day3.csv')

# ee_year=[]
# battery=0
# while battery<15001:
#     rate=0
#     while rate<1.01:
#         i=0
#         ee = []
#         while i<8760:
#             if i==0:
#                 ee.append(0)
#             else:
#                 if ee[i-1]>0:
#                     if per_hour_day3[i]<day4[i]*rate:
#                         if day4[i]*rate-per_hour_day3[i]+ee[i-1]>battery:
#                             ee.append(battery)
#                         else:
#                             ee.append(day4[i]*rate-per_hour_day3[i]+ee[i-1])
#                     else:
#                         if ee[i-1]>per_hour_day3[i]:
#                             ee.append(ee[i-1]-per_hour_day3[i])
#                         else:
#                             ee.append(0)
#                 else:
#                     if per_hour_day3[i]<day4[i]*rate:
#                         ee.append(day4[i]*rate-per_hour_day3[i])
#                     else:
#                         ee.append(0)
#             i=i+1
#         ee_year.append(sum(ee))
#         rate=rate+0.01
#
#     battery=battery+100
#     print(battery)
#
# ee1=np.array(ee_year).reshape(151,101)
#
# file=pd.DataFrame(data=ee1)
# file.to_csv('heatmap.csv')