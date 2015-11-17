#Brunston Poon (c) 2015, MIT License
import numpy as np
from scipy import stats
import math

muk = [0.2364, 0.2199, 0.2313]
std_muk = np.std(muk)

print("stdev of muk:", std_muk)

error_prop_to_theta = math.sqrt((1/((std_muk**2)+1))**2)

print("error propagation to theta:", error_prop_to_theta)
