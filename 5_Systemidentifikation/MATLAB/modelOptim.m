clear all

% Create chirp test signal.
testSig = chirp(linspace(0, 1000, 1000), 0.0001, 1000, 0.05, 'quadratic')';

% Calculate system response.
testResponse = Systems.system4(testSig);

% Define cost function with signle parameter.
costFctn = @(cutoff) sum((testResponse - ...
    Models.filterOptim(testSig, cutoff, 1)).^2);

% Start optimization with initial value of cut-off frequency 0.5.
cutoffFrequOpt = fminsearch(costFctn, 0.1);

% Print results.
disp(cutoffFrequOpt);
