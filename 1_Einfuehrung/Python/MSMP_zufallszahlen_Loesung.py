''' Generierung und Visualisierung von Zufallsprozessen

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''
import numpy as np
import matplotlib.pyplot as plt

N = 200
# 1. Normalverteilt. mu=2, sigma=3
x_nv = np.random.randn(N)*3 + 2
fig1, ax1 = plt.subplots(1, 2, sharey='all', figsize=(9, 4))
ax1[0].stem(x_nv)
ax1[0].set_xlabel('Index n')
ax1[0].set_ylabel('Wert des Zufallsprozesses $x_n[n]$')
ax1[1].hist(x_nv, bins=10, orientation='horizontal', density=True)
ax1[1].set_xlabel('Normierte Häufigkeiten')
plt.title('Normalverteilt. Mittelwert: {:.2f}, STD: {:.2f}'.format(
    np.mean(x_nv), np.std(x_nv)))
plt.show()

# 2. Gleichverteilt.
mu, sigma = 3, 2
width = sigma*np.sqrt(12)
a, b = mu-sigma/2, mu+sigma/2
x_gv = (np.random.rand(N)-0.5)*width + mu
fig2, ax2 = plt.subplots(1, 2, sharey='all', figsize=(9, 4))
ax2[0].stem(x_gv)
ax2[0].set_xlabel('Index n')
ax2[0].set_ylabel('Wert des Zufallsprozesses $x_g[n]$')
ax2[1].hist(x_gv, bins=10, orientation='horizontal', density=True)
ax2[1].set_xlabel('Normierte Häufigkeiten')
plt.title('Gleichverteilt. Mittelwert: {:.2f}, STD: {:.2f}'.format(
    np.mean(x_gv), np.std(x_gv)))
plt.show()

