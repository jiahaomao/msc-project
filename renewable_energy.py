import numpy as np
import matplotlib.pyplot as plt
import random
from house_class import Hr
from house_class import Hs
from solar_stats import solar_stats
from house_class import angle_max
from house_class import phi
import math
import pandas as pd
from house_class import delta


cloud= pd.read_csv('cloud_cover.csv',encoding='utf8',usecols=[2])
cloud1=cloud.iloc[:,0]
cloud_cover=cloud1.tolist()

day=[]
day1=[]
day2=[]
a=0
while a<365:
    t=0
    hour = 0
    hour1 = []
    hour2 = 0
    while t<24:
        if Hr[a]<t<Hs[a]:
            theta=np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta[a])) + np.radians(np.cos(np.radians(phi)) * np.cos(delta[a]) * np.cos(t*15)))) #angle between solar and ground
            AM = 1/np.arccos(np.radians(theta)) #air mass
            x = AM**0.678
            I_D = 1.353*(0.7**x)*1000 #solar radiation
            power=I_D*0.2
            if power<300:
                hour=hour+power

                hour2=power
            else:
                hour=hour+300
                hour2=300
            # hour=hour+3000
            # hour2=3000
        else:
            hour2=0
        t=t+0.01
        day2.append(hour2)
        hour1.append(hour2)
    day.append(hour/100)
    day1.append(hour1)
    a=a+1

year=1
tenyears=[]
sss=day
while year<11:
    i=0
    while i<365:
        tenyears.append(sss[i]*0.99)
        sss[i] = sss[i] * 0.99
        i=i+1
    year=year+1




# d = np.arange(1, 366)
#
# tenyear=np.arange(1,3651)
#
# plt.figure()
# plt.plot(d,day)
# plt.xlabel('day')
# plt.ylabel('Power generation (W)')
# plt.show()
#
# plt.figure()
# plt.plot(tenyear,tenyears)
# plt.xlabel('day')
# plt.ylabel('Power generation (W)')
# plt.show()
#
# plt.figure(2)
#
# plt.subplot(2,1,1)
#
# plt.plot(d,day)
#
# plt.subplot(2,1,2)
#
# plt.plot(tenyear,tenyears)
#


# oneday1=[]
# t=0
# hour = 0
# hour11 = 0
# hour22 = 0
# while t<24:
#     if Hr[200]<t<Hs[200]:
#         theta = np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta[200])) + np.radians(
#             np.cos(np.radians(phi)) * np.cos(delta[200]) * np.cos(t * 15))))
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
#     t=t+0.1
#     oneday1.append(hour11)
#
# oneday2=[]
# while t<24:
#     if Hr[200]<t<Hs[200]:
#         theta = np.arcsin(np.radians(np.sin(0 * np.sin(delta[200])) + np.radians(
#             np.cos(0) * np.cos(delta[200]) * np.cos(t * 15))))
#         AM = 1/np.arccos(np.radians(theta)) #air mass
#         x = AM**0.678
#         I_D = 1.353*(0.7**x)*1000 #solar radiation
#         power=I_D*0.15*np.cos(np.radians(90-phi))
#         if power<300:
#             hour22=power
#         else:
#             hour22=300
#     else:
#         hour22=0
#     t=t+0.01
#     oneday2.append(hour22)
#
# x=np.arange(0,240)
#
# plt.figure()
# plt.plot(x,oneday1)
# plt.plot(x,oneday2)
# plt.show()

# class solar:
#
#     def __init__(self,day_of_year):
#         self.ret_time_solar = []
#         self.ret_val_solar = []
#         self.day_of_year = day_of_year
#         self.solar_panel_power = day[day_of_year]
#
#
#     def get_power_solar_panel(self, t):
#         ret_solar = 0.0
#         # ret_solar = []
#         s = solar_stats()
#         delta = s.get_delta(self.day_of_year)
#         Hr, Hs = s.get_Hr_Hs()
#         asd = []
#         if Hr<t and t<Hs:
#
#             ret_solar = I_D*0.2 + ret_solar
#             return ret_solar
#
#     def get_power_over_day_solar_panel(self):
#         t = 0.0
#         self.ret_time_solar = []
#         self.ret_val_solar = []
#
#         while (t < 24):
#             if (Hr[self.day_of_year - 1] < t < Hs[self.day_of_year - 1]):
#                 self.ret_time_solar.append(t)
#                 self.ret_val_solar.append(self.get_power_solar_panel(t))
#             else:
#                 self.ret_time_solar.append(t)
#                 self.ret_val_solar.append(0)
#
#             t = t + 0.01
#         return self.ret_time_solar, self.ret_val_solar
#
#     def __add__(self, input_obj):
#         ret_solar = solar(self.day_of_year)
#         for i in range(0, len(self.ret_time_solar)):
#             ret_solar.ret_time_solar.append(self.ret_time_solar[i])
#             ret_solar.ret_val_solar.append(self.ret_val_solar[i] + input_obj.ret_val_solar[i])
#         return ret_solar
# #
# generation=[]
# asd=[]
# a=0
#
# while a<365:
#     source_total = solar(a)
#     source_total.get_power_over_day_solar_panel()
#     t_g, val_g = source_total.get_power_over_day_solar_panel()
#
#
#     for i in range(0,1):
#         source1 = solar(a)
#         source1.get_power_over_day_solar_panel()
#         source_total = source1 + source_total
#
#     generation.append(sum(source_total.ret_val_solar))
#     a=a+1

#
#
# generation1=np.array(generation)


# class solar:
#
# 	def __init__(self,day_of_year):
# 		self.ret_time_solar = []
# 		self.ret_val_solar = []
# 		self.day_of_year=day_of_year
# 		self.solar_panel_power = 0#random.uniform(250,300)
#
#
# 	def get_power_solar_panel(self, t):
#
# 		ret_solar = 0.0
# 		#ret_solar = []
# 		s=solar_stats()
# 		delta=s.get_delta(self.day_of_year)
# 		Hr,Hs=s.get_Hr_Hs()
# 		asd=[]
#
# 		if Hr<t and t<Hs:
# 			# theta=np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta)) + np.radians(np.cos(np.radians(phi)) * np.cos(delta) * np.cos(t*15)))) #angle between solar and ground
# 			# AM = 1/np.arccos(np.radians(theta)) #air mass
# 			# x = AM**0.678
# 			# I_D = 1.353*(0.7**x) #solar radiation
# 			# ret_solar = ret_solar+I_D
# 			#ret_solar.append(sum(1.353*pow(0.7, np.nan_to_num(pow(1/np.sin(np.arcsin(np.sin(np.radians(54.664)) * np.sin(delta) + np.cos(phi) * np.cos(delta) * np.cos(t*15))),0.678))*0.2)))
# 			#I_D = 1000 *np.cos(theta)
# 			#ret_solar = ret_solar + 84*5*self.solar_panel_power*(angle_max[self.day_of_year]/max(angle_max))
# 			ret_solar=self.solar_panel_power+ret_solar
#
#
# 			return ret_solar
#
# 	# def rod_test(self):
# 	# 	a=0.0
# 	# 	ret=[]
# 	# 	while a<24.0:
# 	# 		ret.append(self.get_power_solar_panel(a))
# 	# 		a=a+1.0
#
# 	def get_power_over_day_solar_panel(self):
# 		t = 0.0
# 		self.ret_time_solar = []
# 		self.ret_val_solar = []
#
# 		while (t < 24):
# 			if (Hr[self.day_of_year-1]<t<Hs[self.day_of_year-1]):
# 				self.ret_time_solar.append(t)
# 				self.ret_val_solar.append(self.get_power_solar_panel(t))
# 			else:
# 				self.ret_time_solar.append(t)
# 				self.ret_val_solar.append(0)
#
# 			t = t + 0.01
# 		return self.ret_time_solar, self.ret_val_solar
#
#
# 	def __add__(self, input_obj):
# 		ret_solar = solar(self.day_of_year)
# 		for i in range(0, len(self.ret_time_solar)):
# 			ret_solar.ret_time_solar.append(self.ret_time_solar[i])
# 			ret_solar.ret_val_solar.append(self.ret_val_solar[i] + input_obj.ret_val_solar[i])
# 		return ret_solar

# generation=[]
# a=0
# while a<365:
# 	source_total = solar(a)
# 	source_total.get_power_over_day_solar_panel()
# 	t_g, val_g = source_total.get_power_over_day_solar_panel()
#
# 	for i in range(0,2):
# 		source1 = solar(a)
# 		source1.solar_panel_power=3000
# 		source1.get_power_over_day_solar_panel()
# 		source_tot = source1
#
# 	generation.append(sum(source_total.ret_val_solar))
# 	a=a+1
# 	weq=np.array(generation)


