import matplotlib.pyplot as plt
import numpy as np
import math
import random
import folium
import pandas as pd
from house_class import house

class shoting_range(house):

    def __init__(self,day_of_year):
        house.__init__(self,day_of_year)
        self.day_of_year =day_of_year
        self.lamp_power = 0
        self.desktop_power = 0
        self.electric_motor_power = 0
