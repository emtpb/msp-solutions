clear all

% Create chirp test signal
testSig = chirp(linspace(0, 1000, 1000), 0.0001, 1000, 0.05, 'quadratic')';

% Calculate system response.
testResponse = Systems.system4(testSig);

figure;
plot(testSig);
hold on
plot(testResponse);
h = legend('Input signal {\itx}_{in}', 'Output signal {\itx}_{out}');
xlabel('Index $n$')

% Create vectors for parameters.
cutoffFrequVector = linspace(0.001, 0.04, 200);
orderVector = linspace(1, 6, 6);

% Initialize matrix for cost function values.
costFctnEvaled = zeros(length(cutoffFrequVector), length(orderVector));

% Evaluate cost function.
for ii = 1 : length(cutoffFrequVector)
    for jj = 1 : length(orderVector)
        % Apply signal to forward model.
        forwardModelResponse = Models.filter(testSig, ...
            cutoffFrequVector(ii), orderVector(jj));
        % Calculate costs.
        costFctnEvaled(ii, jj) = sum((testResponse - forwardModelResponse).^2);
    end
end

% Create meshgrid for surface plot.
[xs, ys] = meshgrid(orderVector, cutoffFrequVector);

figure;
surf(xs, ys, costFctnEvaled)
xlabel('Filter order {\itn}_{f}')
ylabel('Normalized cut-off frequency \Omega_{c}')
zlabel('Value of cost function')
shading flat
