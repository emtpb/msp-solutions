%% Frequenzbewertung
% In der Akustik werden in einigen Fällen die empfangenen Signale
% frequenzabhängig gewichtet, wobei die Gewichtung den Frequenzgang des
% menschnlichen Gehörs berücksichtigt. Das A-Bewertungsfilter ist im
% Bereich von 20 Hz bis 20 kHz definiert. Stellen Sie den Frequenzgang des
% A-bewerteten Filters im Bereich von 10 Hz bis 100 kHz grafisch dar, wobei
% der Definitionsbereich des Filters von 20 Hz bis 20 kHz beträgt.
%
% Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung
% 
% (c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de

%% Initialisierung
close all; clear all; clc;

%% Variablendefinition
f = logspace(log10(20), log10(20e3), 500);

Ra = 12194^2.*f.^4./((f.^2+20.6.^2) .* (f.^2+12194.^2) .* sqrt(f.^2+107.7^2) .* sqrt(f.^2+737.9.^2));
A = 20*log10(Ra) + 2;

%% Grafische Ausgabe
semilogx(f, A, 'LineWidth', 1.5)
hold on
semilogx([f(1) f(end)], [A(1) A(end)], 'or', 'LineWidth', 1.5)
grid on
xlabel('Frequenz {\itf} / Hz')
ylabel('Frequenzgang |{\itG}| / dB')
title('A-Bewertungsfilter')