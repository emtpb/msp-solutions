import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


# Parameters from the exercise question
f_s = 1e6  # sampling frequency / Hz
N = 5  # filter order
f_c = 10e3  # cutoff frequency / Hz
atten = 40  # stopband attenuation
ripple = 3  # passband ripple

f_Nyq = f_s/2

# Design filters
b_butter, a_butter = signal.butter(N, f_c/f_Nyq)
b_cheby1, a_cheby1 = signal.cheby1(N, ripple, f_c/f_Nyq)
b_cheby2, a_cheby2 = signal.cheby2(N, atten, f_c/f_Nyq)
b_ellip, a_ellip = signal.ellip(N, ripple, atten, f_c/f_Nyq)

# Calculate transfer functions
omega_norm = np.pi * np.arange(0.1*f_c, 10*f_c, 10) / f_Nyq
f_out, G_butter = signal.freqz(b_butter, a_butter, omega_norm)
_, G_cheby1 = signal.freqz(b_cheby1, a_cheby1, omega_norm)
_, G_cheby2 = signal.freqz(b_cheby2, a_cheby2, omega_norm)
_, G_ellip = signal.freqz(b_ellip, a_ellip, omega_norm)

# Calculate transfer function magnitude in dB
G_butter_dB = 20*np.log10(abs(G_butter))
G_cheby1_dB = 20*np.log10(abs(G_cheby1))
G_cheby2_dB = 20*np.log10(abs(G_cheby2))
G_ellip_dB = 20*np.log10(abs(G_ellip))

f_out = f_out * f_Nyq / np.pi

# Draw plots
plt.figure()
plt.semilogx(f_out, G_butter_dB, label='Butterworth')
plt.semilogx(f_out, G_cheby1_dB, label='Cheby 1')
plt.semilogx(f_out, G_cheby2_dB, label='Cheby 2')
plt.semilogx(f_out, G_ellip_dB, label='Ellip')
plt.semilogx(f_out, np.ones(f_out.shape)*-3, '--', label='-3 dB threshold')
plt.semilogx(f_out, np.ones(f_out.shape)*-40, '--', label='Stopband threshold')

plt.xlim((0.1*f_c, 10*f_c))
plt.ylim((-2*atten, 6))
plt.xlabel('Frequency $f$ / Hz')
plt.ylabel('Transfer function magnitude $|G(\mathrm{j}\omega)|$ / dB')
plt.grid(which='both')
plt.legend()
plt.show()

# Find transition band
f_tr = {
    'butter': f_out[np.logical_and(G_butter_dB < -3, G_butter_dB > -40)],
    'cheby1': f_out[np.logical_and(G_cheby1_dB < -3, G_cheby1_dB > -40)],
    'cheby2': f_out[np.logical_and(G_cheby2_dB < -3, G_cheby2_dB > -40)],
    # Note: -40 cannot be used as the lower bound, as that value is reached
    # three times, but we are only interested in the first occurence.
    'ellip': f_out[np.logical_and(G_ellip_dB < -3, G_ellip_dB > -39.99)],
}

# Print transition band properties
print('Transition bands:')
for ftype, freq in f_tr.items():
    print('{}:\t {:.1f} to {:.1f} kHz (width: {:.1f} kHz)'.format(
        ftype, freq[0]/1e3, freq[-1]/1e3, (freq[-1] - freq[0])/1e3))
