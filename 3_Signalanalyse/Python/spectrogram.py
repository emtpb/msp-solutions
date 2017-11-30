import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sio
import scipy.signal as sig

# read and normalize signal
sampl_freq, y = sio.read('head.wav')
y = y/max(y)

# plot signal
t = np.arange(0, len(y))/sampl_freq
plt.figure()
plt.plot(t, y)
plt.xlabel('Zeit $t$ / s')

# calculate spectrogram
f, t, spec = sig.spectrogram(y, fs=sampl_freq, nperseg=512, noverlap=512/2)

# logarithmic scaling and remove inf
spec_log = np.log(abs(spec)**2)
idx_inf = np.isinf(spec_log)
spec_log[idx_inf] = 0

# plot spectrogram
plt.figure()
plt.pcolormesh(t, f, spec_log)
plt.colorbar()
ax = plt.gca()
ax.set_yscale('log')
plt.ylim(f[1], f[-1])
plt.xlabel('Zeit $t$ / s')
plt.ylabel('Frequenz $f$ / Hz')
