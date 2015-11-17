#Brunston Poon (c) 2015, MIT License
import numpy as np
import math

muk = [0.2364, 0.2199, 0.2313]
std_muk = np.std(muk)
avg_muk = np.mean(muk)
error_prop_to_theta = math.sqrt((1/((avg_muk**2)+1))*std_muk)

print("stdev of muk:", std_muk)
print("avg of muk:", avg_muk)
print("error propagation to theta:", error_prop_to_theta)
print("error prop in degrees:", error_prop_to_theta * 180 / math.pi)
