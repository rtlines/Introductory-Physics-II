# Code to plot a Van der Waals isotherm
# This started as a Google AI quirry, it did pertty good
# But I wanted different units.
import numpy as np
import matplotlib.pyplot as plt

Patm=1.013*10**5  #Pa
# Constants for CO2 https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Atomic_and_Molecular_Properties/A8%3A_van_der_Waal's_Constants_for_Real_Gases
a = 3.658  # L^2 atm / mol^2
b = 0.04286 # L / mol
#R = 0.08206  # L atm / (mol K)
n = 1 # Assuming 1 mole for simplicity

# Gas constant in our units
R = 8.314510 #  J mol⁻¹K⁻¹

# convert units for van der walls coefficients

toPa = Patm/1    #Pa/atm
tom3 = 0.001 #1000cm**3 * (1m/100ucm)*83
a = a * toPa * tom3**2
b = b * tom3

print(a, b)  # check these, they match http://www.hsc.edu.kw/student/materials/Physics/website/hyperphysics%20modified/hbase/kinetic/waal.html
             # pretty well
   

# Temperatures
T_high = 330  # Above Tc
T_critical = 304.13
T_low = 290  # Below Tc

# Volume range
#V = np.linspace(0.1, 5, 200) # Adjust range as needed (liters)
V = np.linspace(0.075*tom3, 0.3*tom3, 200) # Adjust range as needed

def van_der_waals_pressure(V, T, a, b, n, R):
    return (n*R*T)/(V-n*b) - a*(n/V)**2

# Calculate and plot isotherms
plt.figure(figsize=(8, 6))

for T in [T_high, T_critical, T_low]:
    P = [van_der_waals_pressure(v, T, a, b, n, R) for v in V]
    plt.plot(V, P, label=f'T = {T} K')

plt.xlabel('Volume (m**3)')
plt.ylabel('Pressure (Pa)')
#plt.title('Van der Waals Gas P-V Diagram')
plt.legend()
plt.grid(True)
plt.show()