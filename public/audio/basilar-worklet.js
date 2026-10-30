// Educational parallel bandpass bank. Not a fluid-structure cochlear solver.
class BasilarBank extends AudioWorkletProcessor {
  constructor() {
    super();
    this.channels = Array.from({length: 96}, (_, i) => {
      const x = i / 95, cf = 165.4 * (10 ** (2.1 * (1-x)) - .88);
      const w = 2*Math.PI*Math.min(cf, sampleRate*.45)/sampleRate;
      const alpha = Math.sin(w)/10, a0 = 1+alpha;
      return {cf, b0: alpha/a0, b2:-alpha/a0, a1:-2*Math.cos(w)/a0,
        a2:(1-alpha)/a0, x1:0,x2:0,y1:0,y2:0, power:0,
        delay:new Float32Array(Math.max(1, Math.round(sampleRate*(.0003+.006*x*x)))), cursor:0, value:0};
    });
    this.frames=0;
  }
  process(inputs) {
    const input=inputs[0];
    if (!input?.length) return true;
    const n=input[0].length;
    for(let s=0;s<n;s++) {
      let v=0;
      for(const ch of input) v+=ch[s]/input.length;
      for(const c of this.channels) {
        const y=c.b0*v+c.b2*c.x2-c.a1*c.y1-c.a2*c.y2;
        c.x2=c.x1;c.x1=v;c.y2=c.y1;c.y1=y;
        c.value=c.delay[c.cursor];c.delay[c.cursor]=y;c.cursor=(c.cursor+1)%c.delay.length;
        c.power=.998*c.power+.002*c.value*c.value;
      }
    }
    // Output remains silent: microphone monitoring is never connected.
    if((this.frames+=n)>=sampleRate/60) {
      this.frames=0;
      this.port.postMessage({values:this.channels.map(c=>c.value), envelope:this.channels.map(c=>Math.sqrt(c.power)), sampleRate});
    }
    return true;
  }
}
registerProcessor('basilar-bank', BasilarBank);
