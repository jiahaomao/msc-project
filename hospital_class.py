import matplotlib.pyplot as plt
import numpy as np
import math
import random
import folium
import pandas as pd
from house_class import house

class hospital(house):

    def __init__(self,day_of_year):
        house.__init__(self,day_of_year)
        self.day_of_year =day_of_year
        self.lamp_power = 0
        self.desktop_power = 0
        self.freezer_power = 0
        self.disinfection_cabinet_power = 0
        self.airconditioner_power = 0
        self.medical_equipment_power = 0
        self.phone_charge_power = 0
        self.printer_power = 0
        self.wireless_power = 0
        self.extractor_fan_power = 0
        self.microwave_power = 0
        self.washing_power = 0
        self.tumble_dryer_power = 0
