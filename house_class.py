#!/usr/bin/env python3`
import random
import numpy as np
#from solar_stats import Hr,Hs,angle_max

d = np.arange(1, 366) #day fo year
for i in d:
    #s= solar_stats()

    #delta =(23.45 * np.sin((2 * np.pi * (284 + d)) / 365))
    delta = np.radians(23.45*np.sin(np.radians((360/365)*(d-81))))
    phi = np.radians(54.664) #Latitude of Chilton
    Hr = 12-((1/15)*np.degrees(np.arccos(-(np.sin(phi)*np.sin(delta))/(np.cos(phi)*np.cos(delta)))))  #sunrise
    Hs = 12+((1/15)*np.degrees(np.arccos(-(np.sin(phi)*np.sin(delta))/(np.cos(phi)*np.cos(delta)))))  #sunset
    sunhours = Hs-Hr  #daytime
    angle_max = np.degrees(np.arcsin(np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta))) #the max angle between solar and ground everyday

    #angle = np.degrees(np.arcsin(np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta) * np.cos())) #angle between solar and ground

class house:


    def __init__(self,day_of_year):
        self.ret_time = []
        self.ret_val = []
        self.per_hour = []
        self.day_of_year = day_of_year


        self.tv_power = 0
        self.tv_on_time1 = random.uniform(6, 9)
        self.tv_off_time1 = self.tv_on_time1 + random.uniform(0.25, 3)
        self.tv_on_time2 = random.uniform(12, 13)
        self.tv_off_time2 = self.tv_on_time2 + random.uniform(0.25, 2)
        self.tv_on_time3 = random.uniform(17, 18)
        self.tv_off_time3 = self.tv_on_time3 + random.uniform(3, 6)


        self.printer_power = 0
        self.printer_on_time = random.uniform(9, 19)
        self.printer_off_time = self.printer_on_time + random.uniform(0.25, 1)

        self.wireless_power = 0
        self.wireless_on_time = 0
        self.wireless_off_time = 24

        self.phone_charge_power = 0
        self.phone_charge_on_time = random.uniform(18, 20)
        self.phone_charge_off_time = self.phone_charge_on_time + random.uniform(2, 4)

        # self.airconditioner_power = 0
        # self.airconditioner_on_time = random.uniform(10, 12)
        # self.airconditioner_off_time = self.airconditioner_on_time + random.uniform(4, 10)

        self.electric_fan_power = 0
        self.electric_fan_on_time = random.uniform(10, 12)
        self.electric_fan_off_time = self.electric_fan_on_time + random.uniform(4, 10)

        self.cooker_hood_power = 0
        self.cooker_hood_on_time1 = random.uniform(6, 8)
        self.cooker_hood_off_time1 = self.cooker_hood_on_time1 + random.uniform(0.25, 0.5)
        self.cooker_hood_on_time2 = random.uniform(17, 19)
        self.cooker_hood_off_time2 = self.cooker_hood_on_time2 + random.uniform(0.25, 1)

        self.extractor_fan_power = 0
        self.extractor_fan_on_time = random.uniform(6, 8)
        self.extractor_fan_off_time = self.extractor_fan_on_time + random.uniform(4, 16)

        self.electric_heater_power = 0
        self.electric_heater_on_time1 = 0
        self.electric_heater_off_time1 = random.uniform(6, 8)
        self.electric_heater_on_time2 = random.uniform(17, 19)
        self.electric_heater_off_time2 = 24

        self.hob_ring_power = 0
        self.hob_ring_on_time1 = random.uniform(6, 8)
        self.hob_ring_off_time1 = self.hob_ring_on_time1 + random.uniform(0.2, 0.3)
        self.hob_ring_on_time2 = random.uniform(11, 12)
        self.hob_ring_off_time2 = self.hob_ring_on_time2 + random.uniform(0.25, 0.5)
        self.hob_ring_on_time3 = random.uniform(17, 18)
        self.hob_ring_off_time3 = self.hob_ring_on_time3 + random.uniform(0.25, 1)

        self.oven_power = 0
        self.oven_on_time = random.uniform(8, 19)
        self.oven_off_time = self.oven_on_time + random.uniform(0.25, 0.75)

        self.microwave_power = 0
        self.microwave_on_time = random.uniform(8, 20)
        self.microwave_off_time = self.microwave_on_time + random.uniform(0.1, 0.25)

        self.toaster_power = 0
        self.toaster_on_time = random.uniform(7, 8)
        self.toaster_off_time = self.toaster_on_time + random.uniform(0.2, 0.6)

        self.coffee_maker_power = 0
        self.coffee_maker_on_time = random.uniform(7, 12)
        self.coffee_maker_off_time = self.coffee_maker_on_time + random.uniform(0.2, 0.8)

        self.juicer_power = 0
        self.juicer_on_time = random.uniform(11, 12)
        self.juicer_off_time = self.juicer_on_time + random.uniform(0.2, 0.8)

        self.kettle_power = 0
        self.kettle_on_time = random.uniform(6, 20)
        self.kettle_off_time = self.kettle_on_time + random.uniform(0.1, 0.25)

        self.lamp_power = 0
        self.lamp_on_time1 = random.uniform(6, 8)
        self.lamp_off_time1 = random.uniform(9, 10)
        self.lamp_on_time2 = random.uniform(16, 18)
        self.lamp_off_time2 = random.uniform(22, 24)

        self.desk_lamp_power = 0
        self.desk_lamp_on_time = random.uniform(17, 19)
        self.desk_lamp_off_time = self.desk_lamp_on_time + random.uniform(4, 5)

        self.desktop_power = 0
        self.desktop_on_time1 = random.uniform(6, 8)
        self.desktop_off_time1 = self.desktop_on_time1 + random.uniform(10, 14)
        self.desktop_on_time2 = random.uniform(19, 20)
        self.desktop_off_time2 = self.desktop_on_time2 + random.uniform(2, 4)

        self.laptop_power = 0
        self.laptop_on_time1 = random.uniform(6, 8)
        self.laptop_off_time1 = self.laptop_on_time1 + random.uniform(8, 10)
        self.laptop_on_time2 = random.uniform(19, 20)
        self.laptop_off_time2 = self.laptop_on_time2 + random.uniform(1, 3)

        self.refrigerator_power = random.choice([120, 130, 150])

        self.dishwasher_power = 0
        self.dishwasher_on_time = random.uniform(18, 19)
        self.dishwasher_off_time = self.dishwasher_on_time + random.uniform(0.5, 1)

        self.washing_power = 0
        self.washing_on_time = random.uniform(20, 20.5)
        self.washing_off_time = self.washing_on_time + random.uniform(1, 2)

        self.tumble_dryer_power = 0
        self.tumble_dryer_on_time = random.uniform(21, 21.5)
        self.tumble_dryer_off_time = self.tumble_dryer_on_time + random.uniform(0.5, 1.5)

        self.hair_dryer_power = 0
        self.hair_dryer_on_time = random.uniform(21, 22)
        self.hair_dryer_off_time = self.hair_dryer_on_time + random.uniform(0.15, 0.4)

        self.hoover_power = 0
        self.hoover_on_time = random.uniform(14, 16)
        self.hoover_off_time = self.hoover_on_time + random.uniform(0.5, 1.5)

        self.amplifier_power = 0
        self.amplifier_on_time = random.uniform(17, 18)
        self.amplifier_off_time = self.amplifier_on_time + random.uniform(3, 5)

        self.freezer_power = 0
        self.freezer_on_time = 0
        self.freezer_off_time = 24

        self.electric_door_power = 0
        self.electric_door_on_time = 9
        self.electric_door_off_time = 17

        self.electric_motor_power = 0
        self.electric_motor_on_time = 9
        self.electric_motor_off_time = 17

        self.disinfection_cabinet_power = 0
        self.disinfection_cabinet_on_time = 9
        self.disinfection_cabinet_off_time = 17

        self.elevator_power = 0
        self.elevator_on_time = 9
        self.elevator_off_time = 17

        self.beauty_instrument_power = 0
        self.beauty_instrument_on_time = 9
        self.beauty_instrument_off_time = 17

        self.medical_equipment_power = 0
        self.medical_equipment_on_time = random.uniform(7, 10)
        self.medical_equipment_off_time = random.uniform(17, 21)

        self.industrial_equipment_power = 0
        self.industrial_equipment_on_time = random.uniform(9, 10)
        self.industrial_equipment_off_time = random.uniform(17, 21)

        self.ATM_power = 0
        self.ATM_on_time = 9
        self.ATM_off_time = 17



    def get_power(self, t):

        ret = 0.0

        if (self.tv_on_time1 <= t < self.tv_off_time1): #or (self.tv_on_time2 <= t < self.tv_off_time2) or (
                #self.tv_on_time3 <= t < self.tv_off_time3):
            ret = ret + self.tv_power
        if (self.printer_on_time <= t < self.printer_off_time):
            ret = ret + self.printer_power
        if (self.wireless_on_time <= t < self.wireless_off_time):
            ret = ret + self.wireless_power
        if (self.phone_charge_on_time <= t < self.phone_charge_off_time):
            ret = ret + self.phone_charge_power
        # if (self.airconditioner_on_time <= t < self.airconditioner_off_time):
        #     ret = ret + self.airconditioner_power * angle_max[self.day_of_year]/max(angle_max)
        if (self.electric_fan_on_time <= t < self.electric_fan_on_time):
            ret = ret + self.electric_fan_power
        if (self.cooker_hood_on_time1 <= t < self.cooker_hood_off_time1) or (
                self.cooker_hood_on_time2 <= t < self.cooker_hood_off_time2):
            ret = ret + self.cooker_hood_power
        if (self.extractor_fan_on_time <= t < self.extractor_fan_off_time):
            ret = ret + self.extractor_fan_power
        if (self.electric_heater_on_time1 <= t < self.electric_heater_off_time1) or (
                self.electric_heater_on_time2 <= t < self.electric_heater_off_time2):
            ret = ret + self.electric_heater_power * (1-angle_max[self.day_of_year]/max(angle_max))
        if (self.hob_ring_on_time1 <= t < self.hob_ring_off_time1) or (
                self.hob_ring_on_time2 <= t < self.hob_ring_off_time2) or (
                self.hob_ring_on_time3 <= t < self.hob_ring_off_time3):
            ret = ret + self.hob_ring_power
        if (self.oven_on_time <= t < self.oven_off_time):
            ret = ret + self.oven_power
        if (self.microwave_on_time <= t < self.microwave_off_time):
            ret = ret + self.microwave_power
        if (self.toaster_on_time <= t < self.toaster_off_time):
            ret = ret + self.toaster_power
        if (self.coffee_maker_on_time <= t < self.coffee_maker_off_time):
            ret = ret + self.coffee_maker_power
        if (self.juicer_on_time <= t < self.juicer_off_time):
            ret = ret + self.juicer_power
        if (self.kettle_on_time <= t < self.kettle_off_time):
            ret = ret + self.kettle_power
        if (self.lamp_on_time1 <= t < self.lamp_off_time1 and t > Hr[self.day_of_year]) or (
                self.lamp_on_time2 <= t < self.lamp_off_time2 and t > Hs[self.day_of_year]):
            ret = ret + self.lamp_power
        if (self.desk_lamp_on_time <= t < self.desk_lamp_off_time and t > Hs[self.day_of_year]):
            ret = ret + self.desk_lamp_power
        if (self.desktop_on_time1 <= t < self.desktop_off_time1) or (
                self.desktop_on_time2 <= t < self.desktop_off_time2):
            ret = ret + self.desktop_power
        if (self.laptop_on_time1 <= t < self.laptop_off_time1) or (
                self.laptop_on_time2 <= t < self.laptop_off_time2):
            ret = ret + self.laptop_power
        if (0 < t < 1) or (3 < t < 4) or (6 < t < 7) or (9 < t < 10) or (12 < t < 13) or (15 < t < 16) or (
                18 < t < 19) or (21 < t < 22):
            ret = ret + self.refrigerator_power * angle_max[self.day_of_year]/max(angle_max)
        if (self.dishwasher_on_time <= t < self.dishwasher_off_time):
            ret = ret + self.dishwasher_power
        if (self.washing_on_time <= t < self.washing_off_time):
            ret = ret + self.washing_power
        if (self.tumble_dryer_on_time <= t < self.tumble_dryer_off_time):
            ret = ret + self.tumble_dryer_power
        if (self.hair_dryer_on_time <= t < self.hair_dryer_off_time):
            ret = ret + self.hair_dryer_power
        if (self.hoover_on_time <= t < self.hoover_off_time):
            ret = ret + self.hoover_power
        if (self.amplifier_on_time <= t < self.amplifier_off_time):
            ret = ret + self.amplifier_power
        if (self.freezer_on_time <= t < self.freezer_off_time):
            ret = ret + self.freezer_power * angle_max[self.day_of_year]/max(angle_max)
        if (self.electric_door_on_time <= t < self.electric_door_off_time):
            ret = ret + self.electric_door_power
        if (self.electric_motor_on_time <= t < self.electric_motor_off_time):
            ret = ret + self.electric_motor_power
        if (self.disinfection_cabinet_on_time <= t < self.disinfection_cabinet_off_time):
            ret = ret + self.disinfection_cabinet_power
        if (self.elevator_on_time <= t < self.elevator_off_time):
            ret = ret + self.elevator_power
        if (self.beauty_instrument_on_time <= t < self.beauty_instrument_off_time):
            ret = ret + self.beauty_instrument_power
        if (self.medical_equipment_on_time <= t < self.medical_equipment_off_time):
            ret = ret + self.medical_equipment_power
        if (self.industrial_equipment_on_time <= t < self.industrial_equipment_off_time):
            ret = ret + self.industrial_equipment_power
        if (self.ATM_on_time <= t < self.ATM_off_time):
            ret = ret + self.ATM_power

        return ret



    def get_power_over_day(self):
        t = 0.0
        self.ret_time = []
        self.ret_val = []

        while (t < 24):
            self.ret_time.append(t)
            self.ret_val.append(self.get_power(t))

            t = t + 0.1

        return self.ret_time, self.ret_val


    # def per_hour_of_year(self):
    #     self.per_hour=[]
    #     d=0
    #     while d<356:
    #         self.per_hour.append(self.get_power_over_day())
    #         # print(d)
    #         d=d+1
    #
    #     return self.per_hour


    def __add__(self, input_obj):
        ret_house = house(self.day_of_year)
        for i in range(0, len(self.ret_time)):
            ret_house.ret_time.append(self.ret_time[i])
            ret_house.ret_val.append(self.ret_val[i] + input_obj.ret_val[i])
            # ret_house.per_hour.append(input_obj.per_hour[i])
        return ret_house

# generation=[]
# a=0
# while a<365:
#     source_total = house(a)
#     source_total.get_power_over_day()
#     t_g, val_g = source_total.get_power_over_day()
#
#     for i in range(0,2):
#         source1 = house(a)
#         source1.ATM_power=3000
#         source1.get_power_over_day()
#         source_total = source1+source_total
#
#     generation.append(sum(source_total.ret_val))
#     a=a+1








