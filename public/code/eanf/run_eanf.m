function [single, duration, paired, trains] = run_eanf()
% After starting AMT 1.6.0, run [single,duration,paired,trains] = run_eanf().
% All currents below are specified in mA and converted to A at the AMT call.
fs = 1e6;
gap = 30;
amps = (0.49:0.01:0.75)';
prob = zeros(size(amps));
for k = 1:numel(amps)
    prob(k) = single_probability(amps(k),100,gap,fs);
end
assert(all(diff(prob)>=0));
single = table(amps,prob,'VariableNames',{'mA','p_spike'});

widths = [25;50;100;200];
threshold = zeros(size(widths));
for k = 1:numel(widths)
    lo = 0.05;
    hi = 4;
    assert(single_probability(lo,widths(k),gap,fs)<0.5 && ...
           single_probability(hi,widths(k),gap,fs)>0.5);
    for step = 1:30
        mid = (lo+hi)/2;
        if single_probability(mid,widths(k),gap,fs)<0.5
            lo = mid;
        else
            hi = mid;
        end
    end
    threshold(k) = (lo+hi)/2;
    assert(abs(single_probability(threshold(k),widths(k),gap,fs)-0.5)<1e-6);
end
duration = table(widths,threshold,threshold.*widths, ...
    'VariableNames',{'phase_us','threshold50_mA','phase_charge_nC'});

intervals = [0.3;0.5;0.75;1;1.5;2;3;5;8];
firstAmps = [0.58 0.72];
probeAmp = threshold(widths==100);
probe = pulse(probeAmp,100,gap);
rows = zeros(numel(intervals)*numel(firstAmps),5);
row = 0;
for amp = firstAmps
    first = pulse(amp,100,gap);
    for delay = intervals'
        pauseSamples = round(delay*1e-3*fs)-numel(first);
        stim = [zeros(100,1);first;zeros(pauseSamples,1);probe;zeros(100,1)];
        d = felsheim2024(stim,fs);
        assert(numel(d)==2);
        row = row+1;
        rows(row,:) = [amp,delay,probeAmp,d(1).total_probability,d(2).total_probability];
    end
end
assert(all(isfinite(rows),'all') && all(rows(:,4:5)>=0 & rows(:,4:5)<=1,'all'));
paired = array2table(rows,'VariableNames', ...
    {'first_mA','onset_interval_ms','probe_mA','p_first','p_probe'});

pulseCount = 12;
rates = [500 1000];
trainRows = zeros(pulseCount*numel(rates),3);
trainPulse = pulse(0.64,100,gap);
for k = 1:numel(rates)
    period = round(fs/rates(k));
    unit = [trainPulse;zeros(period-numel(trainPulse),1)];
    stim = [zeros(100,1);repmat(unit,pulseCount,1);zeros(100,1)];
    d = felsheim2024(stim,fs);
    assert(numel(d)==pulseCount);
    probs = [d.total_probability]';
    assert(all(isfinite(probs) & probs>=0 & probs<=1));
    range = (k-1)*pulseCount+(1:pulseCount);
    trainRows(range,:) = [repmat(rates(k),pulseCount,1),(1:pulseCount)',probs];
end
trains = array2table(trainRows,'VariableNames',{'pps','pulse_number','p_spike'});
end

function p = single_probability(amp,width,gap,fs)
stim = [zeros(100,1);pulse(amp,width,gap);zeros(100,1)];
d = felsheim2024(stim,fs);
assert(numel(d)==1);
p = d.total_probability;
end

function waveform = pulse(amp,width,gap)
% At 1 MHz, an integer duration in microseconds equals the sample count.
waveform = amp*1e-3*[-ones(width,1);zeros(gap,1);ones(width,1)];
assert(abs(sum(waveform))<1e-12);
end
