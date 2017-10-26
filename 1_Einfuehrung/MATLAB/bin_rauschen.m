clear all; close all; clc;

N = 200;
rauschen_bin = sign(randn(N,1));

plot(rauschen_bin,'LineWidth',1.5)
xlabel('Abtastwert {\itn}')
ylabel('{\ity}')
ylim([-1.2 1.2])

