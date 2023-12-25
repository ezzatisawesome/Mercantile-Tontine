import numpy as np
from utils import get_m_prop

earth_leo2mars_capture = 4.3 # km/s
mars_transfer2mars_capture = 0.9 # km/s
mars_capture2mars_leo = 1.4 # km/s

total_delta_v = earth_leo2mars_capture + mars_transfer2mars_capture + mars_capture2mars_leo

print("Total delta-v: ", total_delta_v, "km/s")