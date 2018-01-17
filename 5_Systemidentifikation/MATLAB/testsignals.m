clear all

nSamples = 5000;

% create signals
% gaussian (normal) distribution 
gaussian = randn(nSamples, 1);
% uniform distribution
uniform = 2*rand(nSamples, 1) - 1;
% random binary sequence 
rbs = sign(gaussian);

figure();
subplot(3,1,1)
plot(gaussian);
title('gaussian')
subplot(3,1,2)
plot(uniform)
title('uniform')
ylim([-2 2])
subplot(3,1,3)
plot(rbs)
title('RBS')
ylim([-2 2])
xlabel('Index {\itn}')
grid on


% plot spectra
normFreq = linspace(0, 2, nSamples);
figure();
plot(normFreq, abs(fft(gaussian)));
hold on
plot(normFreq, abs(fft(uniform)));
plot(normFreq, abs(fft(rbs)));
xlim([0 1])
xlabel('Normalized frequency \Omega')
legend('gaussian', 'uniform', 'RBS')
grid on


% plot auto correlation
lagSamples = (-(nSamples-1) : nSamples-1);
figure();
plot(lagSamples, xcorr(gaussian) ./ max(xcorr(gaussian)));
hold on
plot(lagSamples, xcorr(uniform) ./ max(xcorr(uniform)));
plot(lagSamples, xcorr(rbs) ./ max(xcorr(rbs)));
legend('gaussian', 'uniform', 'RBS')
xlabel('Index lag \Delta{\itn}')
ylabel('Normalized autocorrelation')
grid on
