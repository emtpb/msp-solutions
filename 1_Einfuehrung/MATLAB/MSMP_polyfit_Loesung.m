%% Probleme bei polyfit
% Es werden Messdaten des Materialfeuchtemesssystems NIROMM (EMT)
% verwendet. Quarzsand unterschiedlicher Materialfeuchten psi wird mit
% Infrarotimpulsen unterschiedlicher Strahlungswellenlängen bestrahlt und
% die reflektierte Strahlung gemessen. Bei höheren Feuchten wird mehr
% Strahlung durch die Wassermoleküle absorbiert und demnach weniger
% reflektiert. Der Zusammenhang zwischen den Messspannungen und der
% Materialfeuchte soll durch Polynome geeigneten Grades beschrieben werden.
% Problem ist die geeignete Wahl des Polynomgrades. 
% 
% * Materialfeuchten psi von 0 bis 7 %MF (psi, [0 0.3 0.4 0.5
% 0.6 0.7 0.8 0.9 1.0 1.1 1.2 2.0 3.0 4.0 5.0 7.0], 16 Stützstellen)
% * Für diese Übung wird nur Messkanal 1 (u1) betrachtet.
% * Zur Polynomdarstellung ist ein deutlich höher aufgelöster Feuchtevektor
% erforderlich (psi_Werte_hochaufloesend), da nur so eventuelle
% Schwingungen zwischen den nur 16 Stützstellen sichtbar und damit erkennbar
% werden. 
% 
% Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung
% 
% (c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de

%% Version
%   Dateiname: MI_polyfit_Probleme.m
%   19.01.2013 Dietmar Wetzlar

%% Initialisierung
clc; clear all; close all

%% Variablen laden und definieren
load('MSMP_polyfit_messdaten')
delta_psi = 0.1;
psi_hochaufgeloest = -0.5:delta_psi:8;

p_grad = 8;
  

%%
pol_u1_koeff = polyfit(psi, u1, p_grad);
pol_u1 = polyval(pol_u1_koeff, psi_hochaufgeloest);
pol_u2 = polyval(pol_u1_koeff, psi);


%% Grafische Ausgabe
figure(1)
hold on
plot(psi, u1, '.', 'MarkerSize', 12)
plot(psi_hochaufgeloest, pol_u1, 'LineWidth', 2)
plot(psi, pol_u2)
grid on
xlim([-0.1 7.1])
ylim([1.5 3])