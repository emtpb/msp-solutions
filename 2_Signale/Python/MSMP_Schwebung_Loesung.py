"""
Vergleich von Amplitudenmodulation mit und ohne Trägersignal

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung, Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de

@name: MSMP_schwebung.py
@created 25.08.2016
@author: Sergei Olfert
"""

# Initialisierung
import numpy as np
import matplotlib.pyplot as plt


# Variablendefinitionen
f_0 = 200  # Signalfrequenz
f_t = 2e3  # Trägerfrequenz
f_sam = 40.1e3  # Abtastfrequenz
us_max = 1
ut_max = 1

# Zeitvektor erstellen
t_sam = 1/f_sam
t = np.arange(0, 1/f_0*2, t_sam)

# Zeit- und Trägersignal
signal = us_max * np.sin(2*np.pi*f_0*t)
carrier = np.sin(2*np.pi*f_t*t)

am_mt = (ut_max+signal) * carrier
am_ot = signal * carrier

# Frequenzbereich
F_am_mt = np.fft.fft(am_mt)
F_am_ot = np.fft.fft(am_ot)
f = np.arange(0, f_sam, f_sam/len(t))

# Grafische Ausgabe

# plt.figure(1)
# plt.plot(t, carrier, linewidth=1.5, label='Traegersignal')
# plt.plot(t, signal, linewidth=2, label='Signal')
# plt.xlabel('$t / \mathrm{s}$', fontsize=14)
# plt.ylabel('$u(t) / \mathrm{V}$', fontsize=14)
# plt.legend()
# plt.grid(True)

# plt.figure(2)
# plt.plot(t, signal, linewidth=1.5, label='Signal')
# plt.plot(t, carrier, linewidth=1.5, label='Traegersignal')
# plt.plot(t, am_mt, linewidth=2, label='AM mit Traeger')
# plt.xlabel('$t / \mathrm{s}$', fontsize=14)
# plt.ylabel('$u(t) / \mathrm{V}$', fontsize=14)
# plt.legend()
# plt.grid(True)
#
# plt.figure(3)
# plt.plot(t, signal, linewidth=1.5, label='Signal')
# plt.plot(t, carrier, linewidth=1.5, label='Traegersignal')
# plt.plot(t, am_ot, linewidth=2, label='AM ohne Traeger')
# plt.xlabel('$t / \mathrm{s}$', fontsize=14)
# plt.ylabel('$u(t) / \mathrm{V}$', fontsize=14)
# plt.legend()
# plt.grid(True)

fig, ax = plt.subplots(1, 2, figsize=(9, 4))
ax0 = ax[0]
ax0.plot(t, signal, linewidth=1.5, label='Signal')
ax0.plot(t, carrier, linewidth=1.5, label='Traegersignal')
ax0.plot(t, am_ot, linewidth=2, label='AM ohne Traeger')
ax0.plot(t, am_mt, linewidth=2, label='AM mit Traeger')
ax0.set_xlabel('$t / \mathrm{s}$', fontsize=14)
ax0.set_ylabel('$u(t) / \mathrm{V}$', fontsize=14)
ax0.legend()
ax0.grid(True)
f_half = int(len(f)/2)
ax1 = ax[1]
ax1.plot(f[:f_half], np.abs(np.fft.fft(am_ot))[:f_half], label='AM ohne Träger')
ax1.plot(f[:f_half], np.abs(np.fft.fft(am_mt))[:f_half], '--', label='AM mit Träger')
ax1.set_xlim([0, 2500])
ax1.grid(True)
ax1.legend()
ax1.set_xlabel('Frequenz $f / \mathrm{Hz}$', fontsize=14)
ax1.set_ylabel('Amplitude', fontsize=14)
plt.tight_layout()
plt.show()
