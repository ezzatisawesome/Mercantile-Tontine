import numpy as np
from utils import get_m_prop
from constants import g0

# Delta-V values.
earth_leo2mars_capture = 4.3 # km/s
mars_transfer2mars_capture = 0.9 # km/s
mars_capture2mars_leo = 1.4 # km/s
total_delta_v = earth_leo2mars_capture + mars_transfer2mars_capture + mars_capture2mars_leo

# Spacecraft characteristics.
mass_dry = 579000 # kg

# Propulsion charactersitics.
isp = 19436 # s

# Calculations
m_prop = get_m_prop(mass_dry, total_delta_v, isp, g0)
m_prop_frac = m_prop / mass_dry


print("Total delta-v: ", total_delta_v, "km/s")
print("Total mass propellant: ", m_prop, "kg")
print("Propellant fraction: ", m_prop_frac)