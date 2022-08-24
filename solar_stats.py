import numpy as np


class solar_stats:

	def __init__(self):
		pass

	def get_delta(self,d):
		self.delta =np.radians(23.45 * np.sin((2 * np.pi * (284 + d)) / 365))
		return self.delta

	def get_Hr_Hs(self):
		phi = np.radians(54.664) #Latitude of Chilton
		Hr = 12-((1/15)*np.degrees(np.arccos(-(np.sin(phi)*np.sin(self.delta))/(np.cos(phi)*np.cos(self.delta)))))  #sunrise
		Hs = 12+((1/15)*np.degrees(np.arccos(-(np.sin(phi)*np.sin(self.delta))/(np.cos(phi)*np.cos(self.delta)))))  #sunset
		return Hr,Hs

class solar_panel_power:

	def __init__(self,t):
		d = np.arange(1, 366)
		delta = np.radians(23.45 * np.sin(np.radians(360 / 365) * (d - 81)))
		phi = np.radians(54.664)
		theta = np.arcsin(np.radians(np.sin(np.radians(np.radians(phi)) * np.sin(delta)) + np.radians(
			np.cos(np.radians(phi)) * np.cos(delta) * np.cos(t * 15))))  # angle between solar and ground
		AM = 1 / np.arccos(np.radians(theta))  # air mass
		x = AM ** 0.678
		self.I_D = 1.353 * (0.7 ** x)  # solar radiation


	def get_solar_panel_power(self,t):
		ret_soalr_panel_power=0.0
		s=solar_stats()
		Hr,Hs=s.get_Hr_Hs()
		if Hr<t and t<Hs:
			ret_soalr_panel_power=ret_soalr_panel_power+self.I_D
			return ret_soalr_panel_power





'''
d = np.arange(1, 366) #day fo year
for i in d:
    #s= solar_stats()
    delta =np.radians(23.45 * np.sin((2 * np.pi * (284 + d)) / 365))
    #delta = np.radians(23.45*np.sin(np.radians(360/365)*(d-81)))
    phi = np.radians(54.664) #Latitude of Chilton
    Hr = 12-((1/15)*np.degrees(np.arccos(-(np.sin(phi)*np.sin(delta))/(np.cos(phi)*np.cos(delta)))))  #sunrise
    Hs = 12+((1/15)*np.degrees(np.arccos(-(np.sin(phi)*np.sin(delta))/(np.cos(phi)*np.cos(delta)))))  #sunset
    sunhours = Hs-Hr  #daytime
    angle_max = np.degrees(np.arcsin(np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta))) #the max angle between solar and ground everyday
    #angle = np.degrees(np.arcsin(np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta) * np.cos())) #angle between solar and ground
'''