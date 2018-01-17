clear all

% Select system to analyse by setting a function reference. Change to 
% system1 .. system6 to select. 
sys = @Systems.system2;

% Create impulse signal.
impulse = zeros(1000,1);
impulse(10) = 1;

% Create step signal.
step = zeros(1000,1);
step(10:end) = 1;

figure()
% Plot normalized step response.
plot(sys(step) ./ max(sys(step)));
hold on
grid on
% Plot normalized impulse response.
plot(sys(impulse) ./ max(sys(impulse)));
legend('Step response', 'Impulse response')
xlabel('Index {\itn}')

normFreq = linspace(0, 2, numel(impulse));
figure()
% Plot absolute value of transfer function by transforming impulse
% response.
loglog(normFreq, abs(fft(sys(impulse))));
xlabel('Normalized frequency \Omega')
ylabel('|{\itG}(\Omega)|')
% Cut to relevant part (~lower quater)
xlim([0, 0.5])
