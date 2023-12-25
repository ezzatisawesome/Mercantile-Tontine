import numpy as np

# Function to calculate the mass of the propellant
def get_m_prop(m_dry, delta_v, isp, g_not):
    # Getting the mass of the propellant
    m_prop = m_dry * (np.exp(delta_v / (isp * g_not)) - 1)
    return m_prop