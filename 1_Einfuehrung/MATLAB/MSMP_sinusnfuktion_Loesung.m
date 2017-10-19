%% Phasenverschobene Sinusfunktion
% Phasenverschobene Sinusfunktion mit einer Frequenz von 100 Hz und
% 2 V Amplitude
% 
% Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung
% 
% (c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de

%% Version
%   Dateiname: MSMP_BodeDiagramm_Aufgabe.m

%% Initialisierung
close all; clear all; clc;

%% Variablendefinition
t = linspace(0, 0.03, 1000);
f_signal = 100; % Hz

signal = 2 * sin(2*pi*f_signal*t + (pi/4));
sigalAbsSqu = signal.^2;

%% Grafische Ausgabe
figure(1)
plot(t, signal);
hold on
plot(t, sigalAbsSqu, 'r');
xlabel('Zeit {\itt} / s');
ylabel('Spannung {\itu} / V');
legend('Sinusfunktion', 'Betragsquadrat der Sinusfunktion')