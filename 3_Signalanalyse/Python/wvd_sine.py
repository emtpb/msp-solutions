import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
from wvd import wvd

# parameter
sampl_freq = 100
N = 1024
t = np.arange(0, N)/sampl_freq

# create signal
f_1 = 1
f_2 = 5

y_1 = np.sin(2*np.pi*f_1*t)
y_2 = np.sin(2*np.pi*f_2*t)
y = y_1+y_2

# plot signal
plt.figure()
plt.plot(t, y)
plt.xlabel('Time $t$ / s')

# Wigner-Ville-Distribution
[wv, ff, tt] = wvd(sig.hilbert(y), 1, N/2, sampl_freq)

plt.figure()
plt.pcolormesh(tt, ff, abs(wv))
plt.xlabel('Time $t$ / s')
plt.ylabel('Frequency $f$ / Hz')
plt.ylim([0, 6])
plt.xlim([t[0], t[-1]])
plt.show()
