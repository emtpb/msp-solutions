'''
Frequenzgangdarstellung
Der Frequenzgang einer RCL-Schaltung soll grafisch dargestellt werden. Aufgrund des großen Kreisfrequenzbereichs
erfolgt die Darstellung logarithmisch.

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''

import numpy as np
import matplotlib.pyplot as plt

# Variablendefinition
R = 1
L = 1e-3
C = 1e-6
omega = np.logspace(3, 6, 500)

F = R / (R + 1j * omega * L + 1 / (1j * omega * C))

# Grafische Ausgabe
plt.figure()
plt.semilogx(omega, 20 * np.log10(np.abs(F)), linewidth=1.5)
plt.title('Bodediagramm, Betrag')
plt.xlabel('$\omega / \mathrm{s}^{-1}$')
plt.ylabel('Betrag $|F| / \mathrm{dB}$')
plt.grid(True)

plt.figure()
plt.semilogx(omega, np.angle(F), linewidth=1.5)
plt.title('Bodediagramm, Phase')
plt.xlabel('$\omega / \mathrm{s}^{-1}$')
plt.ylabel('Phase $\mathrm{\phi} / \mathrm{rad}$')
plt.grid(True)

plt.show()
