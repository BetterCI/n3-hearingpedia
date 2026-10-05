import * as THREE from 'three';

// A stylized navigation surface, not an anatomical or functional brain atlas.
export function brainSurface(theta:number, phi:number, side=1) {
  const length=Math.sin(theta), x=-158*Math.cos(theta);
  const fold=Math.sin(theta*19+Math.sin(phi*7))*Math.sin(phi*13+theta*3);
  const lowerNotch=18*Math.exp(-(((x-48)/37)**2))*Math.max(0,-Math.cos(phi));
  return new THREE.Vector3(
    x,
    24+(Math.cos(phi)>0?104:78)*Math.pow(length,.72)*Math.cos(phi)+lowerNotch+fold*2.4*length,
    side*(5+83*Math.pow(length,.8)*Math.sin(phi)+fold*3.2*length*Math.sin(phi)),
  );
}

export function brainNodePosition(areaIndex:number, index:number, count:number) {
  const column=areaIndex%3, row=Math.floor(areaIndex/3);
  // Golden-ratio sampling keeps new concepts distributed within their color group.
  const u=(index+.5)/count, v=(index*.61803398875+.23)%1;
  const theta=.32+column*.83+u*.83;
  const phi=(row===0?.3:1.62)+v*1.12;
  return brainSurface(theta,phi,index%4===3?-1:1);
}

export function createBrainScaffold() {
  const lines:{points:THREE.Vector3[];opacity:number}[]=[];
  const trace=(sample:(t:number)=>THREE.Vector3,opacity:number,steps=100)=>{
    lines.push({points:Array.from({length:steps+1},(_,i)=>sample(i/steps)),opacity});
  };
  for(const side of [-1,1]) {
    // Dorsal/ventral silhouettes and the split between the hemispheres.
    for(const phi of [0,Math.PI])trace(t=>brainSurface(t*Math.PI,phi,side),.42);
    // Meandering cortical folds, with shorter branches instead of a wire grid.
    for(let band=0;band<8;band++) {
      trace(t=>{
        const theta=.08+t*(Math.PI-.16);
        const phi=.18+band*.39+Math.sin(theta*12+band*1.7)*.095+Math.sin(theta*5-band)*.065;
        return brainSurface(theta,phi,side);
      },.22);
    }
    for(let branch=0;branch<19;branch++) {
      trace(t=>{
        const phi=.32+(branch%6)*.43+t*.3;
        const theta=.35+Math.floor(branch/6)*.82+Math.sin(t*Math.PI)*.14+(branch%3)*.12;
        return brainSurface(theta,phi,side);
      },.16,25);
    }
    // The lower rear outline and compact folds suggest the cerebellum.
    trace(t=>new THREE.Vector3(92+51*Math.cos(t*Math.PI*2),-72+32*Math.sin(t*Math.PI*2),side*7),.38,100);
    for(let band=0;band<9;band++) {
      const latitude=-Math.PI/2+.12+band*(Math.PI-.24)/8;
      trace(t=>{
        const angle=t*Math.PI*2, radius=Math.cos(latitude);
        return new THREE.Vector3(92+51*radius*Math.cos(angle),-72+32*Math.sin(latitude),side*(7+43*radius*Math.sin(angle/2)));
      },band===4?.25:.16,72);
    }
    // A tapered stem completes the familiar side silhouette.
    for(const edge of [-1,1])trace(t=>new THREE.Vector3(26+t*20+edge*(13-t*5),-58-t*71,side*(8+12*Math.sin(t*Math.PI))),.23,32);
    trace(t=>new THREE.Vector3(38+t*16,-129+Math.sin(t*Math.PI)*-3,side*8),.23,24);
  }
  const points=Array.from({length:1100},(_,i)=>{
    const theta=Math.acos(1-2*(i+.5)/1100), phi=(i*2.3999632297)%Math.PI;
    return brainSurface(theta,phi,i%2?1:-1);
  });
  return {lines,points};
}
