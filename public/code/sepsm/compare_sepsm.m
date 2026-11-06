function [results, comparison] = compare_sepsm(spectrum)
% Request a second output to also compute STOI for the same mixtures.
% Start AMT 1.6.0 first. Requires Signal Processing Toolbox and the
% Counting-16-44p1-mono-15secs.wav sample shipped with Audio Toolbox.
if nargin < 1
    spectrum = "matched";
end
file = which('Counting-16-44p1-mono-15secs.wav');
assert(~isempty(file), 'Install the Audio Toolbox counting sample.');
[source, originalFs] = audioread(file);
fs = 22050;
target = resample(source(1:3*originalFs,1),fs,originalFs);
target = target / rms(target) * 10^(65/20); % AMT demo level convention
time = (0:length(target)-1)' / fs;
stream = RandStream('mt19937ar','Seed',20261106);
% Preserve the target's full-clip magnitude spectrum and randomize phase.
carrier = randn(stream,length(time),1);
switch string(spectrum)
    case "matched"
        noisePhase = angle(fft(carrier));
        carrier = real(ifft(abs(fft(target)) .* exp(1i*noisePhase)));
    case "white"
        % Keep the white carrier as a spectral control.
    otherwise
        error('Choose a matched or white noise spectrum.');
end
maskers = [carrier, carrier .* (1 - cos(2*pi*4*time))];
snrs = [-9 -6 -3 0 3];
values = zeros(numel(snrs)*2,4);
if nargout > 1
    stoi = zeros(size(values,1),1);
end
for m = 1:2
    unitNoise = maskers(:,m) / rms(maskers(:,m));
    for s = 1:numel(snrs)
        noise = unitNoise * rms(target) / 10^(snrs(s)/20);
        assert(abs(20*log10(rms(target)/rms(noise))-snrs(s)) < 1e-9);
        mixture = target + noise;
        longTerm = joergensen2011(mixture,noise,fs);
        multi = joergensen2013(mixture,noise,fs);
        row = (m-1)*numel(snrs)+s;
        if nargout > 1
            stoi(row) = taal2011(target,mixture,fs);
        end
        values(row,:) = [m,snrs(s),longTerm.SNRenv,multi.SNRenv];
    end
end
assert(all(isfinite(values),'all') && all(values(:,3:4)>0,'all'));
results = array2table(values,'VariableNames',{'masker','acoustic_dB','sEPSM','mr_sEPSM'});
if nargout > 1
    comparison = addvars(results,stoi,'NewVariableNames','STOI');
end
end
