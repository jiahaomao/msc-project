import random
import numpy as np
from house_class import Hr
from house_class import Hs
from house_class import phi
from house_class import delta
from solar_stats import solar_stats
import matplotlib.pyplot as plt
import pandas as pd






















a=np.arange(0.0,180.0,0.75)
i=0
power1=[]
power2=[]
power3=[]
while i<240:
    power1.append(300*np.sin(np.radians(a[i])))
    if i<120:
        power2.append(300*np.cos(np.radians(a[i])))
        power3.append(300 * np.sin(np.radians(a[i])) + 300 * np.cos(np.radians(a[i])))
    else:
        power2.append(300*np.cos(np.radians(180-a[i])))
        power3.append(300 * np.sin(np.radians(a[i])) + 300 * np.cos(np.radians(180-a[i])))

    i=i+1

plt.figure()
plt.subplot(3,1,1)
plt.plot(a,power1)
plt.subplot(3,1,2)
plt.plot(a,power2)
plt.subplot(3,1,3)
plt.plot(a,power3)
plt.show()

asdasd



#
# alpha=np.arcsin()
#
#
# oneday1=[]
# t=0
# hour = 0
# hour11 = 0
# hour22 = 0
#
#
#
# while t<24:
#     if Hr[200]<t<Hs[200]:
#         theta = np.arcsin(np.sin(np.radians(np.radians(phi)) * np.sin(delta[200])) + np.radians(
#             np.cos(np.radians(phi)) * np.cos(delta[200]) * np.cos(t * 15)))
#         AM = 1/np.arccos(np.radians(theta)) #air mass
#         x = AM**0.678
#         I_D = 1.353*(0.7**x)*1000 #solar radiation
#         power=I_D*0.15
#         if power<300:
#             hour11=power
#         else:
#             hour11=300
#     else:
#         hour11=0
#     t=t+1
#     oneday1.append(hour11)
#
#
# x=np.arange(0,24)
#
# plt.figure()
# plt.plot(x,oneday1)
# plt.show()
#
#
#
# asdasdasd









day4 = pd.read_csv('day4.csv',encoding='utf8')


data1=day4['0'].tolist()

asdasd
a=[1,2,3,4,5,6,7,8,9,10,11,12]

d=np.array(a).reshape(3,4)
c=np.array(a)/10
n=3
b=c.reshape(-1,n).sum(1)


d = np.arange(1, 366)
# t=12
# theta = np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta)) + np.radians(
#     np.cos(np.radians(phi)) * np.cos(delta) * np.cos(t * 15))))  # angle between solar and ground
# AM = 1 / np.arccos(np.radians(theta))
# x = AM ** 0.678
# I_D = 1.353 * (0.7 ** x)*1000000
# asdasdasd

# d = np.arange(1, 366)
# al = []
# a=0
# day=[]
# day1=[]
# all=[]
# while a<365:
#     t=0
#     day = []
#     while t<24:
#         if Hr[a]<t<Hs[a]:
#             theta = np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta[a])) + np.radians(
#                 np.cos(np.radians(phi)) * np.cos(delta[a]) * np.cos(t * 15))))  # angle between solar and ground
#
#             AM = 1 / np.arccos(np.radians(theta))  # air mass
#             x = AM ** 0.678
#             I_D = (1.353 * (0.7 ** x))*0.2
#             day.append(I_D)
#         else:
#             day.append(0)
#         t=t+0.01
#     day1.append(day)
#     all.append(sum(day))
#     a=a+1
#
# plt.figure()
# plt.plot(d,all)
# plt.show()
# asdasdasd


class B:

    def __init__(self,day_of_year):
        self.ret_time = []
        self.ret_val = []
        self.day_of_year = day_of_year
        self.power=0


    def get_power_solar_panel(self, t):
        ret_solar = 0.0
        # ret_solar = []
        s = solar_stats()
        delta = s.get_delta(self.day_of_year)
        Hr, Hs = s.get_Hr_Hs()
        asd = []

        if (Hr < t < Hs):
            ret_solar = self.power + ret_solar
            return ret_solar

    def get_power_solar_panel_day(self):
        t = 0.0
        self.ret_time = []
        self.ret_val = []

        while (t < 24):
            if (Hr[self.day_of_year - 1] < t < Hs[self.day_of_year - 1]):
                self.ret_time.append(t)
                self.ret_val.append(self.get_power_solar_panel(t))
            else:
                self.ret_time.append(t)
                self.ret_val.append(0)

            t = t + 0.01
        return self.ret_time, self.ret_val

    def __add__(self, input_obj):
        ret_house = B(self.day_of_year)
        for i in range(0, len(self.ret_time)):
            ret_house.ret_time.append(self.ret_time[i])
            ret_house.ret_val.append(self.ret_val[i] + input_obj.ret_val[i])
        return ret_house



generation=[]

a=0
t=0
while a<365:
    source_total = B(a)
    source_total.get_power_solar_panel_day()
    t_g, val_g = source_total.get_power_solar_panel_day()

    for i in range(0,1):
        source1 = B(a)
        theta=np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta[a])) + np.radians(np.cos(np.radians(phi)) * np.cos(delta[a]) * np.cos(t*15)))) #angle between solar and ground
        AM = 1/np.arccos(np.radians(theta)) #air mass
        x = AM**0.678
        I_D = 1.353*(0.7**x) #solar radiation
        source1.power = I_D*0.2

        source1.get_power_solar_panel_day()
        source_total = source1 + source_total

    generation.append(sum(source_total.ret_val))
    a=a+1



generation1=np.array(generation)


plt.figure()
plt.plot(d,generation1)
plt.show()

# asdasdasdasd
# class A:
#     def __init__(self,day_of_year):
#         self.ret_time = []
#         self.ret_val = []
#         self.day_of_year = day_of_year
#
#
#         self.power=0
#         self.timeon= 1#random.uniform(10,100)
#         self.timeoff= 10#random.uniform(100,200)
#
#         self.power1=0
#         self.timeon1=6
#         self.timeoff1=12
#
#     def get_power(self, t):
#
#         ret = 0.0
#         if (self.timeon<t<self.timeoff):
#             ret=ret+self.power
#         if (self.timeon1<t<self.timeoff1):
#             ret=ret+self.power1
#         return ret
#
#     def get_power_over_day(self):
#         t = 0.0
#         self.ret_time = []
#         self.ret_val = []
#
#         while (t < 24):
#             self.ret_time.append(t)
#             self.ret_val.append(self.get_power(t))
#
#             t = t + 1
#
#         return self.ret_time, self.ret_val
#
#     def __add__(self, input_obj):
#         ret_house = A(self.day_of_year)
#         for i in range(0, len(self.ret_time)):
#             ret_house.ret_time.append(self.ret_time[i])
#             ret_house.ret_val.append(self.ret_val[i] + input_obj.ret_val[i])
#         return ret_house
#
# generation=[]
# a=0
# while a<365:
#     source_total = A(a)
#     source_total.get_power_over_day()
#     t_g, val_g = source_total.get_power_over_day()
#
#     for i in range(0,0):
#         source1 = A(a)
#         source1.power = 500
#
#         source1.get_power_over_day()
#         source_total = source1 + source_total
#
#     generation.append(sum(source_total.ret_val))
#     asd=sum(generation)
#     a=a+1




#
#     self.tv_power = random.choice([70, 95, 130, 250])
#     self.printer_power = random.choice([1, 1.5, 1.7])
#     self.wireless_power = random.choice([8, 10, 15])
#     self.phone_charge_power = random.choice([5, 8, 10])
#     self.airconditioner_power = 1000
#     self.electric_fan_power = 50
#     self.cooker_hood_power = 200
#     self.extractor_fan_power = 30
#     self.electric_heater_power = 1500
#     self.hob_ring_power = 1500
#     self.oven_power = random.choice([1500, 1600])
#     self.microwave_power = random.choice([800, 900])
#     self.toaster_power = 800
#     self.coffee_maker_power = 1000
#     self.juicer_power = 1000
#     self.kettle_power = 1500
#     self.lamp_power = 30
#     self.desk_lamp_power = 10
#     self.desktop_power = 150
#     self.laptop_power = 80
#     self.refrigerator_power = random.choice([120, 130, 150])
#     self.dishwasher_power = 1500
#     self.washing_power = 70
#     self.tumble_dryer_power = 1800
#     self.hair_dryer_power = 1500
#     self.hoover_power = 500
#     self.amplifier_power = 100
#     self.freezer_power = random.choice([150, 160, 180])
#     self.electric_door_power = 370
#     self.electric_motor_power = 150
#     self.disinfection_cabinet_power = 500
#     self.elevator_power = 6000
#     self.beauty_instrument_power = 15
#     self.medical_equipment_power = 15000
#     self.industrial_equipment_power = 15000
#     self.ATM_power = 250
#
#
#     house1.tv_power = 0
#     house1.printer_power = 0
#     house1.wireless_power = 0
#     house1.phone_charge_power = 0
#     house1.electric_fan_power = 0
#     house1.cooker_hood_power = 0
#     house1.extractor_fan_power = 0
#     house1.electric_heater_power = 0
#     house1.hob_ring_power = 0
#     house1.oven_power = 0
#     house1.microwave_power = 0
#     house1.toaster_power = 0
#     house1.coffee_maker_power = 0
#     house1.juicer_power = 0
#     house1.kettle_power = 0
#     house1.lamp_power = 0
#     house1.desk_lamp_power = 0
#     house1.desktop_power = 0
#     house1.laptop_power = 0
#     house1.refrigerator_power = 0
#     house1.dishwasher_power = 0
#     house1.washing_power = 0
#     house1.tumble_dryer_power = 0
#     house1.hair_dryer_power = 0
#     house1.hoover_power = 0
#     house1.amplifier_power = 0
#     house1.freezer_power = 0
#     house1.electric_door_power = 0
#     house1.electric_motor_power = 0
#     house1.disinfection_cabinet_power = 0
#     house1.elevator_power = 0
#     house1.beauty_instrument_power = 0
#     house1.medical_equipment_power = 0
#     house1.industrial_equipment_power = 0
#     house1.ATM_power = 0
#
#
#
#
#
#
#
#
#
#
#
# self.tv_power = random.choice([70, 95, 130, 250])
#         self.tv_on_time1 = random.uniform(6, 9)
#         self.tv_off_time1 = self.tv_on_time1 + random.uniform(0.25, 3)
#         self.tv_on_time2 = random.uniform(12, 13)
#         self.tv_off_time2 = self.tv_on_time2 + random.uniform(0.25, 2)
#         self.tv_on_time3 = random.uniform(17, 18)
#         self.tv_off_time3 = self.tv_on_time3 + random.uniform(3, 6)
#
#
#         self.printer_power = random.choice([1, 1.5, 1.7])
#         self.printer_on_time = random.uniform(9, 19)
#         self.printer_off_time = self.printer_on_time + random.uniform(0.25, 1)
#
#         self.wireless_power = random.choice([8, 10, 15])
#         self.wireless_on_time = 0
#         self.wireless_off_time = 24
#
#         self.phone_charge_power = random.choice([5, 8, 10])
#         self.phone_charge_on_time = random.uniform(18, 20)
#         self.phone_charge_off_time = self.phone_charge_on_time + random.uniform(2, 4)
#
#         self.airconditioner_power = 1000
#         self.airconditioner_on_time = random.uniform(10, 12)
#         self.airconditioner_off_time = self.airconditioner_on_time + random.uniform(4, 10)
#
#         self.electric_fan_power = 50
#         self.electric_fan_on_time = random.uniform(10, 12)
#         self.electric_fan_off_time = self.electric_fan_on_time + random.uniform(4, 10)
#
#         self.cooker_hood_power = 200
#         self.cooker_hood_on_time1 = random.uniform(6, 8)
#         self.cooker_hood_off_time1 = self.cooker_hood_on_time1 + random.uniform(0.25, 0.5)
#         self.cooker_hood_on_time2 = random.uniform(17, 19)
#         self.cooker_hood_off_time2 = self.cooker_hood_on_time2 + random.uniform(0.25, 1)
#
#         self.extractor_fan_power = 30
#         self.extractor_fan_on_time = random.uniform(6, 8)
#         self.extractor_fan_off_time = self.extractor_fan_on_time + random.uniform(4, 16)
#
#         self.electric_heater_power = 1500
#         self.electric_heater_on_time1 = 0
#         self.electric_heater_off_time1 = random.uniform(6, 8)
#         self.electric_heater_on_time2 = random.uniform(17, 19)
#         self.electric_heater_off_time2 = 24
#
#         self.hob_ring_power = 1500
#         self.hob_ring_on_time1 = random.uniform(6, 8)
#         self.hob_ring_off_time1 = self.hob_ring_on_time1 + random.uniform(0.2, 0.3)
#         self.hob_ring_on_time2 = random.uniform(11, 12)
#         self.hob_ring_off_time2 = self.hob_ring_on_time2 + random.uniform(0.25, 0.5)
#         self.hob_ring_on_time3 = random.uniform(17, 18)
#         self.hob_ring_off_time3 = self.hob_ring_on_time3 + random.uniform(0.25, 1)
#
#         self.oven_power = random.choice([1500, 1600])
#         self.oven_on_time = random.uniform(8, 19)
#         self.oven_off_time = self.oven_on_time + random.uniform(0.25, 0.75)
#
#         self.microwave_power = random.choice([800, 900])
#         self.microwave_on_time = random.uniform(8, 20)
#         self.microwave_off_time = self.microwave_on_time + random.uniform(0.1, 0.25)
#
#         self.toaster_power = 800
#         self.toaster_on_time = random.uniform(7, 8)
#         self.toaster_off_time = self.toaster_on_time + random.uniform(0.2, 0.6)
#
#         self.coffee_maker_power = 1000
#         self.coffee_maker_on_time = random.uniform(7, 12)
#         self.coffee_maker_off_time = self.coffee_maker_on_time + random.uniform(0.2, 0.8)
#
#         self.juicer_power = 1000
#         self.juicer_on_time = random.uniform(11, 12)
#         self.juicer_off_time = self.juicer_on_time + random.uniform(0.2, 0.8)
#
#         self.kettle_power = 1500
#         self.kettle_on_time = random.uniform(6, 20)
#         self.kettle_off_time = self.kettle_on_time + random.uniform(0.1, 0.25)
#
#         self.lamp_power = 30
#         self.lamp_on_time1 = random.uniform(6, 8)
#         self.lamp_off_time1 = random.uniform(9, 10)
#         self.lamp_on_time2 = random.uniform(16, 18)
#         self.lamp_off_time2 = random.uniform(22, 24)
#
#         self.desk_lamp_power = 10
#         self.desk_lamp_on_time = random.uniform(17, 19)
#         self.desk_lamp_off_time = self.desk_lamp_on_time + random.uniform(4, 5)
#
#         self.desktop_power = 150
#         self.desktop_on_time1 = random.uniform(6, 8)
#         self.desktop_off_time1 = self.desktop_on_time1 + random.uniform(10, 14)
#         self.desktop_on_time2 = random.uniform(19, 20)
#         self.desktop_off_time2 = self.desktop_on_time2 + random.uniform(2, 4)
#
#         self.laptop_power = 80
#         self.laptop_on_time1 = random.uniform(6, 8)
#         self.laptop_off_time1 = self.laptop_on_time1 + random.uniform(8, 10)
#         self.laptop_on_time2 = random.uniform(19, 20)
#         self.laptop_off_time2 = self.laptop_on_time2 + random.uniform(1, 3)
#
#         self.refrigerator_power = random.choice([120, 130, 150])
#
#         self.dishwasher_power = 1500
#         self.dishwasher_on_time = random.uniform(18, 19)
#         self.dishwasher_off_time = self.dishwasher_on_time + random.uniform(0.5, 1)
#
#         self.washing_power = 70
#         self.washing_on_time = random.uniform(20, 20.5)
#         self.washing_off_time = self.washing_on_time + random.uniform(1, 2)
#
#         self.tumble_dryer_power = 1800
#         self.tumble_dryer_on_time = random.uniform(21, 21.5)
#         self.tumble_dryer_off_time = self.tumble_dryer_on_time + random.uniform(0.5, 1.5)
#
#         self.hair_dryer_power = 1500
#         self.hair_dryer_on_time = random.uniform(21, 22)
#         self.hair_dryer_off_time = self.hair_dryer_on_time + random.uniform(0.15, 0.4)
#
#         self.hoover_power = 500
#         self.hoover_on_time = random.uniform(14, 16)
#         self.hoover_off_time = self.hoover_on_time + random.uniform(0.5, 1.5)
#
#         self.amplifier_power = 100
#         self.amplifier_on_time = random.uniform(17, 18)
#         self.amplifier_off_time = self.amplifier_on_time + random.uniform(3, 5)
#
#         self.freezer_power = random.choice([150, 160, 180])
#         self.freezer_on_time = 0
#         self.freezer_off_time = 24
#
#         self.electric_door_power = 370
#         self.electric_door_on_time = 9
#         self.electric_door_off_time = 17
#
#         self.electric_motor_power = 150
#         self.electric_motor_on_time = 9
#         self.electric_motor_off_time = 17
#
#         self.disinfection_cabinet_power = 500
#         self.disinfection_cabinet_on_time = 9
#         self.disinfection_cabinet_off_time = 17
#
#         self.elevator_power = 6000
#         self.elevator_on_time = 9
#         self.elevator_off_time = 17
#
#         self.beauty_instrument_power = 15
#         self.beauty_instrument_on_time = 9
#         self.beauty_instrument_off_time = 17
#
#         self.medical_equipment_power = 15000
#         self.medical_equipment_on_time = random.uniform(7, 10)
#         self.medical_equipment_off_time = random.uniform(17, 21)
#
#         self.industrial_equipment_power = 15000
#         self.industrial_equipment_on_time = random.uniform(9, 10)
#         self.industrial_equipment_off_time = random.uniform(17, 21)
#
#         self.ATM_power = 250
#         self.ATM_on_time = 9
#         self.ATM_off_time = 17



ee_year=[]
battery=0
while battery<15001:
    rate=0
    while rate<1.01:
        i=0
        ee = []
        while i<8760:
            if i==0:
                ee.append(0)
            else:
                if ee[i-1]>0:
                    if per_hour_day3[i]<day4[i]*rate:
                        if day4[i]*rate-per_hour_day3[i]+ee[i-1]>battery:
                            ee.append(battery)
                        else:
                            ee.append(day4[i]*rate-per_hour_day3[i]+ee[i-1])
                    else:
                        if ee[i-1]>per_hour_day3[i]:
                            ee.append(ee[i-1]-per_hour_day3[i])
                        else:
                            ee.append(0)
                else:
                    if per_hour_day3[i]<day4[i]*rate:
                        ee.append(day4[i]*rate-per_hour_day3[i])
                    else:
                        ee.append(0)

            i=i+1

        ee_year.append(sum(ee))
        rate=rate+0.01

    battery=battery+100
    print(battery)

ee1=np.array(ee_year).reshape(151,101)
