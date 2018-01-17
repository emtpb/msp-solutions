clear all

nSamples = 10000;

% Select system to analyze by setting a function reference. Change to 
% system1 .. system6 to select. 
sys = @Systems.system1;

% Create random binary sequence.
rbs = sign(randn(nSamples, 1));

% Apply random binary sequence to selected system.
output = sys(rbs);

% Divide output spectrum by input spectrum.
normFreq = linspace(0, 2, nSamples);
figure()
loglog(normFreq, abs(fft(output) ./ fft(rbs)));
xlabel('Normalized frequency \Omega')
ylabel('|{\itG}(\Omega)|')
xlim([0, 0.5])
hold on
