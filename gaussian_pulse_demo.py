import sys
import numpy as np
import matplotlib.pyplot as plt

# Pulse Parameters
vmax = 5  # volts
fc = 5e9  # GHz
bw = 50  # percent
v0 = 0.00001  # Maximum voltage allowed at t = 0
ptype = 'normal' # pulse type

# Time vector
t = np.linspace(0,5e-9,2001)

# Compute sigma (control's pulse width)
sigma = 1/(2*np.pi*(fc*bw/100)/2.354820045030949);

# Compute mu (time offset)
# Note that this is only approximate for the Differentiated Pulse.
mu = sigma*np.sqrt(-2*np.log(v0/vmax));

if ptype == 'normal':
    pulse = vmax*np.exp(-(t - mu)**2/(2*sigma**2));
elif ptype == 'diff':
    pulse = -vmax/sigma*(t - mu)*np.exp(0.5 - (t - mu)**2/(2*sigma**2));
elif ptype == 'sinmod':
    pulse = vmax*np.exp(-(t - mu)**2/(2*sigma**2))*np.cos(2*np.pi*fc*(t - mu));
else:
    sys.exit('Unsupported pulse type')

plt.plot(t*1e9, pulse)
plt.xlabel('Time (ns)')
plt.ylabel('Amplitude (Volts)')
plt.grid(True)
plt.show()
