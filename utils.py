# Function to calculate the mass of the propellant
def get_m_prop(m_dry, delta_v, isp, g_not):
    # Getting the mass of the propellant
    m_prop = m_dry * (np.exp(delta_v / (isp * g_not)) - 1)
    return m_prop

# Function to calculate thrust
def big_brain(delta_t, isp, m_dry, delta_v, g_not):
    # Getting the mass of the propellant
    m_prop = get_m_prop(m_dry, delta_v, isp, g_not)

    print(delta_t)
    print(delta_v)
    
    # Getting the mass of the rocket
    m_w = m_dry + m_prop
    
    # Getting the thrust
    thrust = (m_w * delta_v) / delta_t

    # Print the thrust Newtons (kg * m/s^2)
    # print("thrust @ t", delta_t, " = ", thrust)
    
    # Returning the thrust
    return thrust 