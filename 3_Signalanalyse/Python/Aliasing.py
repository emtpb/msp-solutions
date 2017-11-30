import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sio

# read wav file
[f_s, y] = sio.read('r2d2whereareyou.wav')

n = np.size(y)
t = np.linspace(0, n/f_s, n)

plt.figure()
plt.plot(t, y)
plt.xlabel('Time $t$ / s')
plt.title('original signal')

delta_f = f_s/n
f = np.arange(0, f_s, delta_f)

plt.figure()
ft = abs(np.fft.fft(y))
plt.plot(f, ft)
plt.xlabel('frequency $f$ / Hz')
plt.title('spectrum of original signal')

# downsample signal
p = 2               # downsampling factor
f_s_new = f_s/p     # new sampling frequency
y_downsample = y[0::p]
n_new = np.size(y_downsample)
t = np.linspace(0, n_new/f_s_new, n_new)

plt.figure()
plt.plot(t, y_downsample)
plt.xlabel('time $t$ / s')
plt.title('signal sampled with '+str(f_s_new)+' Hz')

delta_f_new = f_s_new/n_new
f_new = np.arange(0, f_s_new, delta_f_new)

plt.figure()
plt.plot(f_new, abs(np.fft.fft(y_downsample)))
plt.xlabel('frequency $f$ / Hz')
plt.title('spectrum of signal sampled with '+str(f_s_new)+' Hz')

# write downsampled signal to .wav
sio.write('downsample.wav', int(f_s_new), y_downsample)
plt.show()
