''' Phasenverschobene Sinusfunktion
Phasenverschobene Sinusfunktion mit einer Frequenz von 100 Hz und 2 V Amplitude

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''

import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 1
t = np.linspace(0, 0.02, 1000)

sig = 2 * np.sin(2*np.pi*100*t + np.pi/4)
sig_abs_squ = np.abs(sig)**2

plt.figure(1)
plt.plot(t, sig)
plt.plot(t, sig_abs_squ)
plt.xlabel('Zeit $t$ / s')
plt.ylabel('Spannung $u$ / V')
plt.legend(('Sinusfunktion', 'Betragsquadrat der Sinusfunktion'))
plt.grid(True)
plt.show()
