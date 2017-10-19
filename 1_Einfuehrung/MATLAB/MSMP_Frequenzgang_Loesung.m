%% Frequenzgangdarstellung
% Der Frequenzgang einer RCL-Schaltung soll grafisch dargestellt werden.
% Aufgrund des groﬂen Kreisfrequenzbereichs erfolgt die Darstellung
% logarithmisch.
% 
% Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/‹bung
% 
% (c) Elektrische Messtechnik, Universit‰t Paderborn - http://emt.upb.de

%% Version
%   Dateiname: MSMP_BodeDiagramm_Loesung.m

%% Initialisierung
close all; clear all; clc;

%% Variablendefinition
R = 1;    L = 1e-3;    C = 1e-6;  
omega = logspace(3, 6, 500); 
F = R ./ (R + 1j*omega*L + 1./(1j*omega*C)); 

%% Grafische Ausgabe
figure(1)
semilogx(omega, 20*log10(abs(F)),'LineWidth',1.5); 
title('Bodediagramm, Betrag'); 
xlabel('\omega / s^{-1}');    ylabel('Betrag |F| / dB'); 
grid on

figure(2)
semilogx(omega, angle(F),'LineWidth',1.5);  
title('Bodediagramm, Phase'); 
xlabel('\omega / s^{-1}');    ylabel('Phase {\it\phi} / rad'); 
grid on