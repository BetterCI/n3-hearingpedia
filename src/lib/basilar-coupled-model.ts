// Passive, uniform two-scala 1D transmission-line teaching model.
// exp(i*w*t), p'' + 2*rho*w^2/(h*D)*p = 0, y=p/D.
// Pressure boundary conditions p(0)=1 Pa, p(L)=0; no active process.
export const coupledParameters={length:.035,height:.001,density:1000,massPerArea:.3,dampingRatio:.05};
export function coupledWaveResponse(frequency:number,count=1201){
  const {length:L,height:h,density:rho,massPerArea:m,dampingRatio:zeta}=coupledParameters;
  const dx=L/(count-1), omega=2*Math.PI*frequency;
  const real=new Float64Array(count), imag=new Float64Array(count);
  const cr=new Float64Array(count), ci=new Float64Array(count), er=new Float64Array(count), ei=new Float64Array(count);
  const pr=new Float64Array(count), pi=new Float64Array(count);pr[0]=1;
  for(let i=0;i<count;i++){
    const x=i/(count-1), omega0=2*Math.PI*165.4*(10**(2.1*(1-x))-.88);
    real[i]=m*(omega0*omega0-omega*omega);imag[i]=2*zeta*m*omega0*omega;
  }
  // Complex Thomas elimination; both off-diagonals are 1.
  for(let i=1;i<count-1;i++){
    const d2=real[i]**2+imag[i]**2, factor=dx*dx*2*rho*omega*omega/h;
    const br=-2+factor*real[i]/d2-(i>1?cr[i-1]:0);
    const bi=-factor*imag[i]/d2-(i>1?ci[i-1]:0);
    const norm=br*br+bi*bi, rr=i===1?-1:-er[i-1], ri=i===1?0:-ei[i-1];
    cr[i]=br/norm;ci[i]=-bi/norm;
    er[i]=(rr*br+ri*bi)/norm;ei[i]=(ri*br-rr*bi)/norm;
  }
  for(let i=count-2;i>=1;i--){pr[i]=er[i]-cr[i]*pr[i+1]+ci[i]*pi[i+1];pi[i]=ei[i]-cr[i]*pi[i+1]-ci[i]*pr[i+1];}
  const result=Array.from({length:count},(_,i)=>{
    const norm=real[i]**2+imag[i]**2;
    const re=(pr[i]*real[i]+pi[i]*imag[i])/norm, im=(pi[i]*real[i]-pr[i]*imag[i])/norm;
    return {x:i/(count-1),re,im,amplitude:Math.hypot(re,im)};
  });
  const peak=Math.max(...result.map(p=>p.amplitude));
  return result.map(p=>({x:p.x,re:p.re/peak,im:p.im/peak,amplitude:p.amplitude/peak}));
}
