#!/usr/bin/env python3
import random

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from PIL import Image, ImageDraw


from house_class import house
from house_class import d
from shop_class import shop
from shoting_range_class import shoting_range
from bar_class import bar
from post_office_class import post_office
from beauty_salon_class import beauty_salon
from library_class import library
from pharmacy_class import pharmacy
from hospital_class import hospital
from restaurant_class import restaurant
from factory_class import factory
from school_class import school
from renewable_energy import day
from house_class import phi
from house_class import delta







test=True

if test==True:
    max_house=5
    max_mid_house=8
    max_big_house = 2
    max_single_house=2
    max_empty_house = 2
    max_fam_house=10
    max_work_from_home_house=3
else:
    max_house = 500
    max_mid_house = 800
    max_big_house = 200
    max_single_house = 300
    max_empty_house = 200
    max_fam_house = 1000
    max_work_from_home_house = 300

area=False
if area==True:
    shop1=12
    shoting_range1=10
    bar1=8
    post_office1=1
    beauty_salon1=3
    library1=1
    pharmacy1=1
    hospital1=1
    restaurant1=7
    factory1=15
    school1=2
    fac=20
else:
    shop1=0
    shoting_range1=0
    bar1=0
    post_office1=0
    beauty_salon1=0
    library1=0
    pharmacy1=0
    hospital1=0
    restaurant1=0
    factory1=0
    school1=0
    fac=0






#thetal_1 = np.arange(193, 366, 1)
#thetal_2 = np.arange(1, 193, 1)
#thetal = np.append(thetal_2, thetal_1)

#for i in thetal:
#    angle_c = thetal/(np.around(sunhours*60, decimals=5)/2)

consumption=[]
generation=[]
extra_electricity=[]
lack_electricity=[]
battery_electricity=[]
lack=0
extra=0
battery=0
per_hour1=[]
summer=[]
winter=[]


a=0
t=0
while a<365:


    house_total = house(a)
    house_total.get_power_over_day()
    t_c, val_c = house_total.get_power_over_day()

    # source_total = solar(a)
    # source_total.get_power_over_day_solar_panel()
    # t_g, val_g = source_total.get_power_over_day_solar_panel()



    # empty
    for i in range(0, max_empty_house):
        house1 = house(a)
        house1.wireless_power = 10
        house1.refrigerator_power = 120

        house1.get_power_over_day()
        house_total = house1 + house_total

    # single house
    for i in range(0, max_single_house):
        house1 = house(a)
        house1.tv_power = 70
        house1.wireless_power = 8
        house1.phone_charge_power = 5
        house1.electric_fan_power = 50
        house1.cooker_hood_power = 200
        house1.extractor_fan_power = 30
        house1.oven_power = 1500
        house1.microwave_power = 800
        house1.coffee_maker_power = 1000
        house1.lamp_power = 30 * 5
        house1.desk_lamp_power = 10 * 2
        house1.laptop_power = 80
        house1.refrigerator_power = 120
        house1.washing_power = 70
        house1.tumble_dryer_power = 1000
        house1.hoover_power = 300
        house1.get_power_over_day()
        house_total = house_total + house1

    # small house
    for i in range(0, max_house):
        house1 = house(a)
        house1.tv_power = 70
        house1.wireless_power = 8
        house1.phone_charge_power = 5
        house1.electric_fan_power = 50
        house1.cooker_hood_power = 200
        house1.extractor_fan_power = 30
        house1.oven_power = 1500
        house1.microwave_power = 800
        house1.coffee_maker_power = 1000
        house1.lamp_power = 30 * 5
        house1.desk_lamp_power = 10 * 2
        house1.laptop_power = 80
        house1.refrigerator_power = 120
        house1.washing_power = 70
        house1.tumble_dryer_power = 1000
        house1.hoover_power = 500
        house1.toaster_power = 800
        house1.kettle_power = 1500
        house1.hair_dryer_power = 1500
        house1.get_power_over_day()
        house_total = house_total + house1

    # middle house
    for i in range(0, max_mid_house):
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

    # big house
    for i in range(0, max_big_house):
        house1 = house(a)
        house1.tv_power = 95 * 2
        house1.printer_power = 1.5
        house1.wireless_power = 10 * 2
        house1.phone_charge_power = 15
        house1.electric_fan_power = 30
        house1.cooker_hood_power = 200 * 2
        house1.extractor_fan_power = 50 * 4
        house1.electric_heater_power = 1500
        house1.hob_ring_power = 1500 * 2
        house1.oven_power = 1500
        house1.microwave_power = 800
        house1.toaster_power = 800
        house1.coffee_maker_power = 1000
        house1.juicer_power = 1000
        house1.kettle_power = 1500
        house1.lamp_power = 30 * 20
        house1.desk_lamp_power = 10 * 5
        house1.desktop_power = 150
        house1.laptop_power = 80*2
        house1.refrigerator_power = 120 * 2
        house1.dishwasher_power = 1500
        house1.washing_power = 70
        house1.tumble_dryer_power = 1800
        house1.hair_dryer_power = 1500
        house1.hoover_power = 600
        house1.amplifier_power = 100
        house1.get_power_over_day()
        house_total = house_total + house1


    # family house
    for i in range(0, max_fam_house):
        house1 = house(a)
        house1.phone_charge_power = 5 * 6



        house1.get_power_over_day()
        house_total = house_total + house1

    # work from  house
    for i in range(0, max_work_from_home_house):
        house1 = house(a)
        house1.desktop_power = 150
        house1.laptop_power = 80 * 2
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, shop1):
        house1 = shop(a)
        house1.freezer_power = 160 * 6
        house1.desktop_power = 150 * 5
        house1.lamp_power = 30 * 20
        house1.airconditioner_power = 3000 * 4
        house1.ATM_power = 250
        house1.electric_door_power = 370
        house1.printer_power = 1.7 * 5
        house1.refrigerator_power = 120 * 4
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, shoting_range1):
        house1 = shoting_range(a)
        house1.lamp_power = 30 * 50
        house1.desktop_power = 150 * 4
        house1.electric_motor_power = 1500 * 4
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, bar1):
        house1 = bar(a)
        house1.lamp_power = 30 * 20
        house1.airconditioner_power = 3000 * 2
        house1.tv_power = 95 * 2
        house1.desktop_power = 150 * 3
        house1.freezer_power = 160 * 2
        house1.refrigerator_power = 120 * 2
        house1.amplifier_power = 100 * 6
        house1.disinfection_cabinet_power = 500 * 2
        house1.phone_charge_power = 5 * 10
        house1.wireless_power = 10 * 5
        house1.extractor_fan_power = 30 * 4
        house1.coffee_maker_power = 1000 * 2
        house1.juicer_power = 1000 * 4
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, post_office1):
        house1 = post_office(a)
        house1.desktop_power = 150 * 10
        house1.lamp_power = 30 * 20
        house1.printer_power = 1.7 * 2
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, beauty_salon1):
        house1 = beauty_salon(a)
        house1.beauty_instrument_power = 15 * 10
        house1.airconditioner_power = 1000 * 4
        house1.disinfection_cabinet_power = 500
        house1.lamp_power = 30 * 10
        house1.tv_power = 95 * 3
        house1.desktop_power = 150 * 2
        house1.amplifier_power = 100 * 4
        house1.phone_charge_power = 5 * 5
        house1.wireless_power = 10 * 2
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, library1):
        house1 = library(a)
        house1.lamp_power = 30 * 100
        house1.desktop_power = 150 * 10
        house1.printer_power = 1.7 * 5
        house1.wireless_power = 10 * 10
        house1.microwave_power = 800
        house1.get_power_over_day()
        house_tot = house_total + house1

    for i in range(0, pharmacy1):
        house1 = pharmacy(a)
        house1.freezer_power = 160 * 3
        house1.desktop_power = 150 * 2
        house1.lamp_power = 30 * 8
        house1.printer_power = 1.7 * 2
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, hospital1):
        house1 = hospital(a)
        house1.lamp_power = 30 * 1000
        house1.desktop_power = 150 * 50
        house1.freezer_power = 160 * 10
        house1.disinfection_cabinet_power = 500 * 10
        house1.airconditioner_power = 3000 * 100
        house1.medical_equipment_power = 15000 * 10
        house1.phone_charge_power = 5 * 100
        house1.printer_power = 1.7 * 10
        house1.wireless_power = 10 * 50
        house1.extractor_fan_power = 30 * 4
        house1.microwave_power = 800 * 2
        house1.washing_power = 70 * 6
        house1.tumble_dryer_power = 1800 * 6
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, restaurant1):
        house1 = restaurant(a)
        house1.lamp_power = 30 * 50
        house1.amplifier_power = 100 * 6
        house1.airconditioner_power = 3000 * 2
        house1.desktop_power = 150 * 2
        house1.disinfection_cabinet_power = 500
        house1.phone_charge_power = 5 * 10
        house1.wireless_power = 10 * 3
        house1.extractor_fan_power = 30 * 10
        house1.oven_power = 1600 * 4
        house1.microwave_power = 800 * 2
        house1.coffee_maker_power = 1000 * 2
        house1.juicer_power = 1000 * 2
        house1.refrigerator_power = 120 * 2
        house1.freezer_power = 160 * 2
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, factory1):
        house1 = factory(a)
        house1.lamp_power = 30 * 1000
        house1.desktop_power = 150 * 100
        house1.airconditioner_power = 3000 * 30
        house1.elevator_power = 6000 * 2
        house1.industrial_equipment_power = 15000 * 10
        house1.phone_charge_power = 5 * 200
        house1.printer_power = 1.7 * 10
        house1.wireless_power = 10 * 50
        house1.microwave_power = 800 * 2
        house1.get_power_over_day()
        house_total = house_total + house1

    for i in range(0, school1):
        house1 = school(a)
        house1.tv_power = 95 * 20
        house1.desktop_power = 150 * 10
        house1.amplifier_on_time = 100 * 20
        # house1.airconditioner_power = 1000 * 25
        house1.lamp_power = 30 * 50
        house1.phone_charge_power = 5 * 350
        house1.printer_power = 1.7 * 2
        house1.wireless_power = 10 * 5
        house1.extractor_fan_power = 30 * 6
        house1.microwave_power = 800 * 2
        house1.refrigerator_power = 120
        house1.get_power_over_day()
        house_total = house_total + house1

    # for i in range(0,max_house+max_mid_house+max_big_house+max_single_house+max_empty_house):
    #     source1 = solar(a)
    #     theta=np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta[a])) + np.radians(np.cos(np.radians(phi)) * np.cos(delta[a]) * np.cos(t*15)))) #angle between solar and ground
    #     AM = 1/np.arccos(np.radians(theta)) #air mass
    #     x = AM**0.678
    #     I_D = 1.353*(0.7**x)*1000 #solar radiation
    #     if I_D*0.2<300:
    #         source1.power = I_D*0.2*10/100
    #     else:
    #         source1.power = 30
    #
    #     source1.get_power_over_day_solar_panel()
    #     source_total = source1 + source_total

    #print(source_total.ret_val_solar)
    # if sum(house_total.ret_val)>sum(source_total.ret_val_solar):
    #     lack=lack+(sum(house_total.ret_val)-sum(source_total.ret_val_solar))
    #     battery=0
    # else:
    #     extra=extra+(sum(source_total.ret_val_solar)-sum(house_total.ret_val))
    #     if sum(source_total.ret_val_solar)-sum(house_total.ret_val)>8000*(max_house+max_mid_house+max_big_house+max_single_house+max_empty_house):
    #         battery=8000*(max_house+max_mid_house+max_big_house+max_single_house+max_fam_house+max_work_from_home_house)
    #     else:
    #         battery=sum(source_total.ret_val_solar)-sum(house_total.ret_val)

    gen=day[a]*(max_house+max_mid_house*1.2+max_big_house*1.5+max_single_house+max_fam_house+max_work_from_home_house+
                shoting_range1+bar1+post_office1+beauty_salon1+library1+pharmacy1+hospital1+restaurant1+factory1*10+school1*10+fac*10)*20


    # +shop1+shoting_range1+bar1+post_office1+beauty_salon1+library1+pharmacy1+hospital1+restaurant1+factory1+school1

    if sum(house_total.ret_val)>gen:
        lack=lack+(sum(house_total.ret_val)-gen)
        battery=0
    else:
        extra=extra+(gen-sum(house_total.ret_val))
        if gen-sum(house_total.ret_val)>8000*(max_house+max_mid_house+max_big_house+max_single_house+max_fam_house+max_work_from_home_house+shoting_range1+bar1+post_office1+beauty_salon1+library1+pharmacy1+hospital1+restaurant1+factory1+school1+fac):
            battery=8000*(max_house+max_mid_house+max_big_house+max_single_house+max_fam_house+max_work_from_home_house+shop1+shoting_range1+bar1+post_office1+beauty_salon1+library1+pharmacy1+hospital1+restaurant1+factory1+school1+fac)
        else:
            battery=gen-sum(house_total.ret_val)

    per_hour1.append(house_total.ret_val)
    consumption.append(sum(house_total.ret_val))
    generation.append(gen)
    extra_electricity.append(gen-sum(house_total.ret_val))
    lack_electricity.append(sum(house_total.ret_val)-gen)
    battery_electricity.append(battery)
    #y_c = np.array(consumption)

    #y_g = np.array(generation)
    if a==160:
        summer=house_total.ret_val
    elif a==355:
        winter=house_total.ret_val


    a = a+1
    print(a)


print('extra electricity = ',extra)
print('lacking electricity = ',lack)


all=sum(consumption)
consumption_d=np.array(consumption)
generation_d=np.array(generation)
extra_electricity_d=np.array(extra_electricity)
lack_electricity_d=np.array(lack_electricity)
battery_electricity_d=np.array(battery_electricity)


# test = pd.DataFrame(data=consumption)
# test.to_csv('consumption.csv',encoding='utf-8')



#figure 1
plt.figure(1)
plt.plot(d,consumption_d,color='b',label='consumption')
plt.plot(d,generation_d,color='k',label='generation')
plt.fill_between(d,consumption_d,generation_d,where=(consumption_d > generation_d),facecolor='r',alpha=0.7,interpolate=True)
plt.fill_between(d,consumption_d,generation_d,where=(consumption_d < generation_d),facecolor='g',alpha=0.3,interpolate=True)
plt.legend()
plt.xlabel('day')
plt.ylabel('W')
#figure 2



# plt.figure(2)
#
# plt.subplot(3,1,1)
# plt.axhline(y=0,color='r')
# plt.plot(day,extra_electricity_d)
#
#
# plt.subplot(3,1,2)
# plt.axhline(y=0,color='r')
# plt.plot(day,lack_electricity_d)
#
# plt.subplot(3,1,3)
# plt.plot(day,battery_electricity_d)
#
#
#
# plt.figure(3)
# # plt.plot(d,consumption_d,color='b',label='consumption')
# # plt.plot(d,generation_d,color='k',label='generation')
# # plt.fill_between(d,consumption_d,generation_d,where=(consumption_d > generation_d),facecolor='r',alpha=0.7,interpolate=True)
# # plt.fill_between(d,consumption_d,generation_d,where=(consumption_d < generation_d),facecolor='g',alpha=0.3,interpolate=True)
# # plt.legend()
# plt.plot(day,consumption_d)
# plt.xlim(0,365)
# plt.xlabel('day')
# plt.ylabel('W')
#
# plt.figure(4)
# t=np.arange(0,240)
# # plt.plot(d,consumption_d,color='b',label='consumption')
# # plt.plot(d,generation_d,color='k',label='generation')
# # plt.fill_between(d,consumption_d,generation_d,where=(consumption_d > generation_d),facecolor='r',alpha=0.7,interpolate=True)
# # plt.fill_between(d,consumption_d,generation_d,where=(consumption_d < generation_d),facecolor='g',alpha=0.3,interpolate=True)
# # plt.legend()
# plt.plot(t,summer,t,winter)
# plt.xlim(0,240)
# plt.xlabel('hour')
# plt.ylabel('W')
# plt.show()


#im1= Image.open("H:\\pythonProject\\Chilton.png")
#im1 = im1.resize((500,500))
#draw =ImageDraw.Draw(im1)
#draw.polygon([(254,688),(234,728),(288,778),(341,706),(302,672),(288,704)],fill=(255,0,0,128))
#draw.polygon([(308,602),(356,552),(608,504),(608,303),(306,256),(257,405)],fill=(255,255,0,128))
#draw.polygon([(106,106),(108,207),(302,256),(353,56),(306,6),(258,2)],fill=(255,0,255,128))
