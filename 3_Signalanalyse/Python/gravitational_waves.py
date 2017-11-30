import numpy as np
import matplotlib.pyplot as plt
from wavelet_transform import wavelet_transform

# load data
lines = np.loadtxt("H1.txt", comments="#")
t = lines[:, 0]
y = lines[:, 1]
sampl_freq = 1/(t[1]-t[0])

plt.figure()
plt.plot(t, y)
plt.xlabel('Time $t$ / s')
plt.ylabel('Strain $\epsilon\cdot 1e-21$')

delta_f = sampl_freq/len(y)
f = np.arange(-sampl_freq/2, sampl_freq/2, delta_f)
y_fft = abs(np.fft.fftshift(np.fft.fft(y)))

plt.figure()
plt.plot(f, y_fft)
plt.xlabel('Frequency $f$ / Hz')
plt.ylabel('Betragsspekrum')


# %%
# define wavelet parameters
f_c = 50
f_b = 1/50/2
scales = np.linspace(1/10, 10, num=1000)


def wavelet_fun(f):
    # define wavelet function (complex morlet)
    return np.exp(-f_b ** 2 * np.pi ** 2 * (f - f_c) ** 2)

# compute wavelet transform
wt = wavelet_transform(y, sampl_freq, scales, wavelet_fun)

plt.figure()
plt.pcolormesh(t, f_c/scales, abs(wt))
plt.xlabel('Time $t$ / s')
plt.ylabel('Frequency $f$ / Hz')

plt.show()
