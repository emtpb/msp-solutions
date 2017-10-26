%% Signum-Funktion
% Erstellen einer Signum-Funktion der Länge N mit dem Sprung an der Stelle
% M
%
%
% Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung, Übung
%
% (c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de

function x = MSMP_signum(N, M)

x = ones(1, N);
x(1 : M-1) = 0;

end