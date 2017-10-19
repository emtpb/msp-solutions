'''
Frequenzbewertung
In der Akustik werden in einigen Fällen die empfangenen Signale
frequenzabhängig gewichtet, wobei die Gewichtung den Frequenzgang des
menschnlichen Gehörs berücksichtigt. Das A-Bewertungsfilter ist im
Bereich von 20 Hz bis 20 kHz definiert. Stellen Sie den Frequenzgang des
A-bewerteten Filters im Bereich von 10 Hz bis 100 kHz grafisch dar, wobei
der Definitionsbereich des Filters von 20 Hz bis 20 kHz beträgt.

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''

import numpy as np
import matplotlib.pyplot as plt

# Variablendefinition
a, b, c, d, e = 12194, 20.6, 107.7, 737.9, 12194  # in Hz
f = np.logspace(np.log10(20), np.log10(20e3), 500)

Ra = a**2*f**4./((f**2+b**2) * np.sqrt(f**2+c**2) * np.sqrt(f**2+d**2) * (f**2+e**2))
A = 20 * np.log10(Ra) + 2

# Grafische Augabe
plt.figure(1)
plt.semilogx(f, A, linewidth=1.5)
plt.semilogx(f[0], A[0], 'ro')
plt.semilogx(f[-1], A[-1], 'ro')
plt.grid(True)
plt.xlabel('Frequenz $f / \mathrm{Hz}$')
plt.ylabel('Frequenzgang $|G| / \mathrm{dB}$')
plt.title('Bewertungsfilter A')
plt.show()
