# Code to plot the planck function for an object at 0C and 
# an object that is glowin red 1200C and one that is glowing blue 600C
# This started as a Google AI quirry, it did pertty good
# But I wanted different units.
import numpy as np
import matplotlib.pyplot as plt


   

# Temperatures
T_Red = 273.15 +1200  # Above Tc
T_0 = 273.15
T_Blue = 273.15 +6000  # Below Tc

# Volume range
#V = np.linspace(0.1, 5, 200) # Adjust range as needed (liters)
wavelengths_nm = np.linspace(200, 1000, 200) # in nanometers
# but I need this in meters
wavelengths_m = wavelengths_nm *10**(-9)

def Calculate_Planck_Function(lam, T):
    # lam is wavelength in microns
    # T is temperature in kelvin
    c = 3*10**8  # m/s
    h = 6.6260755*10**(-34)  #Js
    k = 1.3806568*10**(-23)  #J/K
    c1=2*np.pi*h*c**2
    c2=h*c/k
    x=c2/(lam*T)
    return c1/(lam**5*(np.exp(x)-1))

# Calculate and plot isotherms
plt.figure(figsize=(8, 6))

B_Red = [Calculate_Planck_Function(lam,T_Red) for lam in wavelengths_m]
B_Red_max =np.max(B_Red)

B_Blue = [Calculate_Planck_Function(lam,T_Blue) for lam in wavelengths_m]
B_Blue_max =np.max(B_Blue)

B_0 = [Calculate_Planck_Function(lam,T_0) for lam in wavelengths_m]
B_0_max=np.max(B_0)

plt.plot(wavelengths_nm, B_0/B_0_max,'k')
plt.plot(wavelengths_nm, B_Red/B_Red_max,'r')
plt.plot(wavelengths_nm, B_Blue/B_Blue_max,'b')

plt.xlabel('Lambda (nm)')
plt.ylabel('I/I_max')
#plt.title('Van der Waals Gas P-V Diagram')
plt.legend()
plt.grid(True)
#plt.xlim(0,2)
plt.show()