import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {references} from '../src/data/references.ts';
import {waveResponse,displayedCyclesPerSecond,advanceWavePhase} from '../src/scripts/basilar-wave.ts';
import {coupledWaveResponse} from '../src/lib/basilar-coupled-model.ts';
const code=readFileSync('public/audio/basilar-worklet.js','utf8');
function bank(fs){
  let Processor;
  const scope={sampleRate:fs,Float32Array,Math,AudioWorkletProcessor:class{constructor(){this.port={postMessage:data=>{this.latest=data;}};}},registerProcessor:(_,p)=>Processor=p};
  vm.runInNewContext(code,scope);
  return new Processor();
}
const results=[];
for(const slowdown of[1000,2000,4000]){
  for(const f of[60,500,1000,3000,16000]){
    assert.equal(displayedCyclesPerSecond(f*2,slowdown)/displayedCyclesPerSecond(f,slowdown),2);
    // At a quarter displayed period the phase must be pi/2, for every frequency.
    const quarterPeriod=slowdown/(4*f);
    assert(Math.abs(advanceWavePhase(0,quarterPeriod,f,slowdown)-Math.PI/2)<1e-12);
    // Equal elapsed time must agree at different rendering frame rates.
    let phase30=0,phase144=0;
    for(let i=0;i<30;i++)phase30=advanceWavePhase(phase30,.37/30,f,slowdown);
    for(let i=0;i<144;i++)phase144=advanceWavePhase(phase144,.37/144,f,slowdown);
    assert(Math.abs(phase30-phase144)<1e-10);
  }
}
for(const fs of[44100,48000])for(const frequency of[500,1000,3000]){
  const p=bank(fs);const block=new Float32Array(128);
  for(let n=0;n<fs;n+=128){for(let j=0;j<128;j++)block[j]=.15*Math.sin(2*Math.PI*frequency*(n+j)/fs);p.process([[block]]);}
  const d=p.latest;assert(d&&d.values.length===96&&d.envelope.every(Number.isFinite));
  const peak=d.envelope.indexOf(Math.max(...d.envelope));
  const expected=(1-Math.log10(frequency/165.4+.88)/2.1)*95;
  assert(Math.abs(peak-expected)<=1,'Pure-tone peak does not match frequency-place map');
  // A center-frequency sine should have RMS near amplitude/sqrt(2), allowing CF discretization.
  assert(d.envelope[peak]>.08&&d.envelope[peak]<.12);
  // Animated figure uses the exact complex transfer function, including integer delay.
  const analytic=waveResponse(frequency,96,fs), finalSample=Math.ceil(fs/128)*128-1;
  for(let i=0;i<96;i++){
    const phase=2*Math.PI*frequency*finalSample/fs;
    const predicted=.15*(analytic[i].re*Math.sin(phase)+analytic[i].im*Math.cos(phase));
    assert(Math.abs(predicted-p.channels[i].value)<1e-4,'Animated figure differs from audio filter response');
  }
  for(let n=0;n<fs/2;n+=128)p.process([[new Float32Array(128)]]);
  assert(Math.max(...p.latest.envelope)<1e-5,'Filter bank failed to settle to silence');
  results.push({fs,frequency,peak,expected,rms:d.envelope[peak]});
}
const dual=bank(48000), b=new Float32Array(128);
for(let n=0;n<48000;n+=128){for(let j=0;j<128;j++)b[j]=.15*(Math.sin(2*Math.PI*500*(n+j)/48000)+Math.sin(2*Math.PI*3000*(n+j)/48000));dual.process([[b]]);}
for(const f of[500,3000]){const i=Math.round((1-Math.log10(f/165.4+.88)/2.1)*95);assert(dual.latest.envelope[i]>.07,'Missing dual-tone response');}
const stereo=bank(48000);for(let n=0;n<30;n++)stereo.process([[b,Float32Array.from(b,v=>-v)]]);
assert(stereo.latest.envelope.every(v=>v===0),'Stereo averaging differs from documented behavior');
const text=readFileSync('src/content/concepts/basilar-membrane.md','utf8');
const independent=JSON.parse(readFileSync('docs/research/basilar-membrane-2026-10-30/coupled-reference.json','utf8'));
for(const check of independent.checks){
  const computed=coupledWaveResponse(check.frequency);
  const refined=coupledWaveResponse(check.frequency,2401);
  let maxComplexError=0;
  for(let i=0;i<computed.length;i++){
    maxComplexError=Math.max(maxComplexError,Math.hypot(computed[i].re-refined[2*i].re,computed[i].im-refined[2*i].im));
    // Every instantaneous harmonic snapshot must remain inside its own envelope.
    for(const phase of[0,.7,2.3,5.8])assert(Math.abs(computed[i].re*Math.cos(phase)-computed[i].im*Math.sin(phase))<=computed[i].amplitude+1e-12);
  }
  assert(maxComplexError<.005,'Complex response has not converged to within 0.5% of normalized peak');
  for(const sample of check.samples){
    assert(Math.abs(computed[sample.index].re-sample.re)<1e-9&&Math.abs(computed[sample.index].im-sample.im)<1e-9,'Coupled solver differs from independent SciPy solution');
  }
  assert(computed.every(p=>Number.isFinite(p.amplitude)&&p.amplitude<=1+1e-12));
  assert(computed.at(-1).amplitude===0,'Apical short-circuit boundary violated');
  assert(Math.abs(check.peak_fraction-check.fine_grid_peak_fraction)<.002,'Spatial grid not converged');
  if(check.frequency>=250&&check.frequency<=3000)assert(check.basal_halfwidth_mm>2*check.apical_halfwidth_mm,'Expected asymmetric passive-wave envelope');
}
const ids=JSON.parse(text.match(/^references: (.+)$/m)[1]);
for(const [_,number,id] of text.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)/g))assert(ids[Number(number)-1]===id&&references[id],`Citation mismatch ${id}`);
for(const [_,slug] of text.matchAll(/\]\(\.\.\/([^/]+)\/\)/g))assert(readFileSync(`src/content/concepts/${slug}.md`));
mkdirSync('docs/research/basilar-membrane-2026-10-30',{recursive:true});
writeFileSync('docs/research/basilar-membrane-2026-10-30/validation.json',JSON.stringify({tests:['proportional animation frequency, quarter period and frame-rate independence','pure-tone place and RMS at 44.1/48 kHz','filterbank complex response versus audio output','passive coupled solver versus independent SciPy solution','coupled-model boundary, normalization, asymmetry and spatial grid convergence','silence decay','dual-tone response','anti-phase stereo downmix','citations and concept links'],results},null,2)+'\n');
console.log('Basilar membrane: DSP, citation and concept-link checks passed.');
