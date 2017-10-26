%% Vergleich von Amplitudenmodulation mit und ohne Trägersignal
%
% Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung
% 
% (c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de

%% Initialisierung
close all; clear all; clc;

%% Variablendefinition
f_0 = 200;      % Signalfrequenz
f_t = 2e3;      % Trägerfrequenz
f_abt = 40.1e3; % Abtastfrequenz
us_max = 1;
ut_max = 1;  

%% Zeitvektor erstellen
t_abt = 1/f_abt;
t = 0 : t_abt : 1/f_0*3;

%% Zeit- und Trägersignal
signal = us_max * sin(2*pi*f_0*t);
traeger = sin(2*pi*f_t*t);

am_mt = (ut_max+signal) .* traeger;
am_ot = signal .* traeger;

%% Grafische Ausgabe
figure(1)
hold on
plot(t, signal, 'linewidth', 1.5)
plot(t, traeger, 'linewidth', 1.5)
xlabel('\itt / s', 'fontsize', 14)
ylabel('\it{u(t)} / V', 'fontsize', 14)
legend('Signal', 'Traegersignal')
grid on

figure(2)
plot(t, signal, 'linewidth', 0.5)
hold on
plot(t, traeger, 'linewidth', 0.5)
plot(t, am_mt, 'k', 'linewidth', 1.5)
xlabel('\itt / s', 'fontsize', 14)
ylabel('\it{u(t)} / V', 'fontsize', 14)
legend('Signal', 'Traegersignal', 'AM mit Traeger')
grid on

figure(3)
plot(t, signal, 'linewidth', 0.5)
hold on
plot(t, traeger, 'linewidth', 0.5)
plot(t, am_ot, 'k', 'linewidth', 2)
xlabel('\itt / s', 'fontsize', 14)
ylabel('\it{u(t)} / V', 'fontsize', 14)
legend('Signal', 'Traegersignal', 'AM ohne Traeger')
grid on

figure(4)
hold on
% plot(t, signal, 'linewidth', 1.0)
% plot(t, traeger, 'linewidth', 1.5)
plot(t, am_ot, 'linewidth', 1.5)
plot(t, am_mt, 'linewidth', 1.5)
xlabel('\itt / s', 'fontsize', 14)
ylabel('\it{u(t)} / V', 'fontsize', 14)
legend('AM mit Traeger', 'AM ohne Traeger')
grid on
