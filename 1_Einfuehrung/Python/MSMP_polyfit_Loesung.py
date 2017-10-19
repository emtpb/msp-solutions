"""
Probleme bei polyfit
Es werden Messdaten des Materialfeuchtemesssystems NIROMM (EMT)
verwendet. Quarzsand unterschiedlicher Materialfeuchten psi wird mit
Infrarotimpulsen unterschiedlicher Strahlungswellenlängen bestrahlt und
die reflektierte Strahlung gemessen. Bei höheren Feuchten wird mehr
Strahlung durch die Wassermoleküle absorbiert und demnach weniger
reflektiert. Der Zusammenhang zwischen den Messspannungen und der
Materialfeuchte soll durch Polynome geeigneten Grades beschrieben werden.
Problem ist die geeignete Wahl des Polynomgrades.

* Materialfeuchten psi von 0 bis 7 %MF (psi, [0 0.3 0.4 0.5
0.6 0.7 0.8 0.9 1.0 1.1 1.2 2.0 3.0 4.0 5.0 7.0], 16 Stützstellen)
* Für diese Übung wird nur Messkanal 1 (u1) betrachtet.
* Zur Polynomdarstellung ist ein deutlich höher aufgelöster Feuchtevektor
erforderlich (psi_Werte_hochaufloesend), da nur so eventuelle
Schwingungen zwischen den nur 16 Stützstellen sichtbar und damit erkennbar
werden.

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
"""

import numpy as np
import matplotlib.pyplot as pp
import scipy.io

# Variablen laden und definieren
mat = scipy.io.loadmat('MSMP_polyfit_messdaten')
psi = mat['psi'][0]
u1 = mat['u1'][0]

delta_psi = 0.1
psi_hochaufgeloest = np.arange(-0.5, 8, delta_psi)

p_grad = 8

#
pol_u1_koeff = np.polyfit(psi, u1, p_grad)
pol_u1 = np.polyval(pol_u1_koeff, psi_hochaufgeloest)
pol_u2 = np.polyval(pol_u1_koeff, psi)

# Grafische Ausgabe
pp.figure()
pp.plot(psi, u1, '.', markersize=12)
pp.plot(psi, pol_u2, linewidth=1.5)
pp.plot(psi_hochaufgeloest, pol_u1, linewidth=1.5)
pp.grid(True)
pp.xlim([-0.1, 7.1])
pp.ylim([1.5, 3])
pp.xlabel('Materialfeuchtigkeit $\psi$')
pp.ylabel('Spannung $u_1$')
pp.legend(['Messwerte', 'polyfit', 'polyfit hd'])

pp.show()
