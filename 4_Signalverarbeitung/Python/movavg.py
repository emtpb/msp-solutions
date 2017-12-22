import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
from scipy import signal

# Load measurement data
data_file = sio.loadmat('ma_filtering.mat', squeeze_me=True)
t = data_file['t']
u = data_file['u']

# Calculate sampling frequency
# Note: All values of diff(t) should be equal (equidistant sampling!), but
#       there can be small numerical errors - hence the mean().
f_s = round(1/np.diff(t).mean())


### Part 1 ###
# Define filter coefficients for order N = 2
N = 2
b_2 = np.ones((N,)) / N

# Apply the filter
u_out_2 = signal.lfilter(b_2, 1, u)  # a = 1 because of FIR filter

# Plot the results
plt.figure()
plt.plot(t*1e3, u, label='Unfiltered')
plt.plot(t*1e3, u_out_2, label='$N$ = 2')
plt.xlim((0, 0.2))
plt.ylim((-1.1, 1.1))
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.legend()
plt.grid()
plt.show()


### Part 2 ###
# Define and apply some more filters with higher order
b_5 = np.ones((5,)) / 5
b_10 = np.ones((10,)) / 10
u_out_5 = signal.lfilter(b_5, 1, u)
u_out_10 = signal.lfilter(b_10, 1, u)

# Plot the results
plt.figure()
plt.plot(t*1e3, u, label='Unfiltered')
plt.plot(t*1e3, u_out_2, label='$N$ = 2')
plt.plot(t*1e3, u_out_5, label='$N$ = 5')
plt.plot(t*1e3, u_out_10, label='$N$ = 10')
plt.xlim((0, 0.2))
plt.ylim((-1.1, 1.1))
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.legend()
plt.grid()
plt.show()

# Problem, visible esp. for N = 10: phase offset!

# Filter again using filtfilt and N = 10
u_filtfilt = signal.filtfilt(b_10, 1, u)

plt.figure()
plt.plot(t*1e3, u, label='Unfiltered')
plt.plot(t*1e3, u_out_10, label='$N$ = 10')
plt.plot(t*1e3, u_filtfilt, label='$N$ = 10, filtfilt')
plt.xlim((0, 0.2))
plt.ylim((-1.1, 1.1))
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.legend()
plt.grid()
plt.show()

# Comparison is not fair: filtfilt-signal is much smoother than the other.
# Why? filtfilt performs double filtering, thus doubling the effective filter
# order! For a fair comparison, compare filtfilt with N = 10 to a lfilter with
# N = 20.

b_20 = np.ones((20,)) / 20
u_out_20 = signal.lfilter(b_20, 1, u)

plt.figure()
plt.plot(t*1e3, u, label='Unfiltered')
plt.plot(t*1e3, u_filtfilt, label='$N$ = 10, filtfilt')
plt.plot(t*1e3, u_out_20, label='$N$ = 20')
plt.xlim((0, 0.2))
plt.ylim((-1.1, 1.1))
plt.xlabel('Time $t$ / ms')
plt.ylabel('Voltage $u$ / V')
plt.legend()
plt.grid()
plt.show()
