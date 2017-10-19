'''
Vergleich verschiedener Methoden zur numerischen Integration

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''
import numpy as np
import scipy.integrate as sci

x_min, x_max = 0, 1
x = np.linspace(x_min, x_max, 5)
y = x**2
dx = x[1] - x[0]

# sum
print('Sum: ' + str(np.sum(y)*dx))

# trapz
print('Trapz: ' + str(np.trapz(y, x)))

# Numerische Integration
y_f = lambda x: x**2
print('Numerische Integration: ' + str(sci.quad(y_f, x_min, x_max)[0]))
