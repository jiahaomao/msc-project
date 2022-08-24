import matplotlib.pyplot as plt
import numpy as np
import math
import random
import folium
import pandas as pd
from house_class import house

class beauty_salon(house):

    def __init__(self,day_of_year):
        house.__init__(self,day_of_year)
        self.day_of_year =day_of_year
        self.beauty_instrument_power = 0
        self.airconditioner_power = 0
        self.disinfection_cabinet_power = 0
        self.lamp_power = 0
        self.tv_power = 0
        self.desktop_power = 0
        self.amplifier_power = 0
        self.phone_charge_power = 0
        self.wireless_power = 0