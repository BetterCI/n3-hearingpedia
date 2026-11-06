function [sweep, profile] = run_carney()
% Requires AMT 1.6.0 (including Zilany MEX functions) and MATLAB.
% Run amt_start before [sweep,profile] = run_carney().
fs = 100000;
t = (0:round(.5*fs)-1)'/fs;
keep = (round(.1*fs)+1):length(t); % 400 ms, whole modulation cycles
modHz = [0 10 20 30 40 50 60 75 90 100 110 125 150 175 200 250 300 400 500];
bmfs = [50 100 200];
rows = zeros(numel(modHz)*numel(bmfs),8);
k = 0;
for bmf = bmfs
    for fm = modHz
        drive = 150*(1 + .8*sin(2*pi*fm*t)); % fm=0 is an unmodulated control
        [be,bs,cn] = carney2015(drive,bmf,fs);
        [beLinear,bsLinear] = carney2015(drive,bmf,fs,'no_ic_hwr');
        k = k+1;
        rows(k,:) = [bmf,fm,mean(drive(keep)),mean(cn(keep)),mean(be(keep)), ...
            mean(bs(keep)),mean(beLinear(keep)),mean(bsLinear(keep))];
    end
end
assert(all(isfinite(rows),'all') && all(rows(:,4:6)>=0,'all'));
assert(max(abs(rows(:,3)-150))<1e-8);
sweep = array2table(rows,'VariableNames',{'bmf_Hz','fm_Hz','an_mean','cn_mean', ...
    'be_mean','bs_mean','be_no_rect','bs_no_rect'});

% Source-filter illustration: one harmonic series with two imposed spectral peaks.
cf = 400:100:2600;
f0 = 100;
targets = [1400 1900];
t = (0:round(.2*fs)-1)'/fs;
keep = (round(.08*fs)+1):round(.18*fs);
taper = ones(size(t));
edge = round(.005*fs);
ramp = (1-cos(linspace(0,pi,edge)'))/2;
taper(1:edge) = ramp;
taper(end-edge+1:end) = flipud(ramp);
rows = zeros(numel(cf)*numel(targets),7);
for j = 1:numel(targets)
    h = 1:40;
    freq = h*f0;
    envelope = .06+exp(-.5*((freq-500)/100).^2)+exp(-.5*((freq-targets(j))/145).^2);
    pressure = (cos(2*pi*t*freq)*(envelope./sqrt(h))').*taper;
    pressure = pressure*(20e-6*10^(65/20)/rms(pressure));
    assert(abs(20*log10(rms(pressure)/20e-6)-65)<1e-9);
    rng(1400,'twister');
    an = zilany2014(pressure,fs,cf,'human','shera2002','fixedFGn','approxPL', ...
        'fiberType',3,'nrep',1,'fsmod',fs,'silent');
    [be,bs,cn] = carney2015(an,100,fs);
    slice = an(keep,:);
    % Fundamental amplitude of periodic rate fluctuations, in rate units.
    f0Amp = 2*abs(mean(slice.*exp(-2i*pi*f0*t(keep)),1));
    idx = (j-1)*numel(cf)+(1:numel(cf));
    rows(idx,:) = [repmat(targets(j),numel(cf),1),cf',mean(slice,1)', ...
        f0Amp',mean(cn(keep,:),1)',mean(be(keep,:),1)',mean(bs(keep,:),1)'];
end
assert(all(isfinite(rows),'all') && all(rows(:,3:end)>=0,'all'));
profile = array2table(rows,'VariableNames',{'upper_peak_Hz','cf_Hz','an_mean', ...
    'an_f0_amplitude','cn_mean','be_mean','bs_mean'});
end
