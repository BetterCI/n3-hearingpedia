import * as THREE from 'three';

// Educational silhouette inspired by cerebral lobes, sulci, cerebellum and stem.
// Procedural navigation geometry, not patient anatomy or a functional brain atlas.
export function brainSurface(theta:number, phi:number, side=1) {
  const length=Math.max(0,Math.sin(theta)), x=-158*Math.cos(theta);
  const upper=103*Math.pow(length,.64)*(1+.055*Math.exp(-Math.pow((x+25)/78,2)));
  const temporal=19*Math.exp(-Math.pow((x+35)/67,2));
  const lower=(62+temporal)*Math.pow(length,.68);
  const center=26+13*Math.exp(-Math.pow((x-105)/58,2));
  const phase=theta*22+phi*3+1.8*Math.sin(phi*5)+.75*Math.sin(theta*9+phi*4);
  const folds=(2.8*Math.cos(phase)+1.1*Math.sin(phi*25+theta*5))*length*Math.sin(phi);
  const central=4.5*Math.exp(-Math.pow((theta-(1.46+.09*Math.cos(phi*3)))/.032,2))*Math.sin(phi);
  const lateralPhi=1.87-.13*(theta-1.5)+.085*Math.sin(theta*3);
  const lateral=5.8*Math.exp(-Math.pow((phi-lateralPhi)/.035,2))*Math.sin(theta)**2;
  const relief=folds-central-lateral;
  const radius=83*Math.pow(length,.73)*(1+.07*Math.exp(-Math.pow((x+70)/68,2)));
  return new THREE.Vector3(
    x,
    center+((Math.cos(phi)>0?upper:lower)+relief)*Math.cos(phi),
    side*(4.8+(radius+relief)*Math.sin(phi)),
  );
}

function hemisphereGeometry(side:number) {
  const positions:number[]=[],indices:number[]=[];
  const rows=104,columns=76;
  for(let i=0;i<=rows;i++)for(let j=0;j<=columns;j++) {
    const p=brainSurface(i/rows*Math.PI,j/columns*Math.PI,side);
    positions.push(p.x,p.y,p.z);
  }
  for(let i=0;i<rows;i++)for(let j=0;j<columns;j++) {
    const a=i*(columns+1)+j,b=a+columns+1;
    if(side>0)indices.push(a,a+1,b,b,a+1,b+1);
    else indices.push(a,b,a+1,b,b+1,a+1);
  }
  const geometry=new THREE.BufferGeometry();
  geometry.setAttribute('position',new THREE.Float32BufferAttribute(positions,3));
  geometry.setIndex(indices);geometry.computeVertexNormals();
  return geometry;
}

export function brainNodePositions(count:number) {
  const positions:THREE.Vector3[]=[];
  const candidates=Array.from({length:49*33},(_,i)=>brainSurface(
    .1+Math.floor(i/33)*(Math.PI-.2)/48,
    .12+(i%33)*(Math.PI-.24)/32,
  ));
  const scores=[candidates.map(()=>Infinity),candidates.map(()=>Infinity)];
  // Alternate hemispheres globally; contiguous color groups also balance.
  // Farthest-point sampling follows the actual curved surface rather than a flat grid.
  for(let i=0;i<count;i++) {
    const sideIndex=i%2, side=sideIndex===0?1:-1;
    let best=0;
    if(i===0)best=16*33+12;
    else for(let j=1;j<candidates.length;j++)if(scores[sideIndex][j]>scores[sideIndex][best])best=j;
    const position=candidates[best].clone();position.z*=side;positions.push(position);
    for(let hemisphere=0;hemisphere<2;hemisphere++)for(let j=0;j<candidates.length;j++) {
      const candidate=candidates[j], z=candidate.z*(hemisphere===0?1:-1);
      const projectedDistance=(candidate.x-position.x)**2+(candidate.y-position.y)**2;
      const distance=projectedDistance+(z-position.z)**2;
      // Offset rear nodes too, keeping the transparent side view from stacking pairs.
      const separation=hemisphere===sideIndex?distance:Math.min(distance,projectedDistance*1.44+28**2);
      scores[hemisphere][j]=Math.min(scores[hemisphere][j],separation);
    }
  }
  return positions;
}

export function createBrainScaffold() {
  const lines:{points:THREE.Vector3[];opacity:number}[]=[];
  const trace=(sample:(t:number)=>THREE.Vector3,opacity:number,steps=100)=>{
    lines.push({points:Array.from({length:steps+1},(_,i)=>sample(i/steps)),opacity});
  };
  for(const side of [-1,1]) {
    // Hemisphere cleft and lateral silhouette stay legible from different views.
    for(const phi of [0,Math.PI/2,Math.PI])trace(t=>brainSurface(t*Math.PI,phi,side),phi===Math.PI/2?.28:.46);
    // Prominent central and lateral grooves break up the rounded lobes.
    trace(t=>{const phi=.09+t*1.86;return brainSurface(1.46+.09*Math.cos(phi*3),phi,side);},.58);
    trace(t=>{const theta=.24+t*2.37;return brainSurface(theta,1.87-.13*(theta-1.5)+.085*Math.sin(theta*3),side);},.55);
    // Short, branching sulci follow different orientations rather than a wire grid.
    for(let fold=0;fold<17;fold++) {
      const column=fold%6,row=Math.floor(fold/6);
      trace(t=>{
        const theta=.22+column*.45+.19*Math.sin(t*Math.PI)+.055*Math.sin(t*9+fold);
        const phi=.17+row*.56+t*.63+.09*Math.sin(t*8+fold*1.8);
        return brainSurface(theta,phi,side);
      },.32,48);
    }
    for(let fold=0;fold<11;fold++) {
      trace(t=>{
        const theta=.24+(fold%4)*.62+t*.47;
        const phi=2.09+Math.floor(fold/4)*.29+.07*Math.sin(t*8+fold);
        return brainSurface(theta,phi,side);
      },.27,42);
    }
    for(let branch=0;branch<16;branch++) {
      trace(t=>brainSurface(.35+(branch%6)*.44+t*.23,.36+Math.floor(branch/6)*.62+.1*Math.sin(t*Math.PI+branch),side),.23,26);
    }
    // Compact folia in the posterior, inferior cerebellum.
    trace(t=>new THREE.Vector3(100+55*Math.cos(t*Math.PI*2),-65+35*Math.sin(t*Math.PI*2),side*6),.44);
    for(let band=0;band<15;band++) {
      const latitude=-Math.PI/2+.13+band*(Math.PI-.26)/14;
      trace(t=>{const angle=t*Math.PI,r=Math.cos(latitude);return new THREE.Vector3(100+55*r*Math.cos(angle),-65+35*Math.sin(latitude)+1.2*Math.sin(angle*7+band),side*(6+49*r*Math.sin(angle)));},.3,64);
    }
  }
  const stem=new THREE.CatmullRomCurve3([new THREE.Vector3(18,-43,0),new THREE.Vector3(25,-66,0),new THREE.Vector3(23,-88,0),new THREE.Vector3(31,-119,0),new THREE.Vector3(34,-137,0)]);
  const stemPositions:number[]=[],stemIndices:number[]=[];
  for(let i=0;i<=40;i++) {
    const t=i/40,p=stem.getPoint(t),radius=13-6*t+5*Math.exp(-Math.pow((t-.28)/.17,2));
    for(let j=0;j<=16;j++){const a=j/16*Math.PI*2;stemPositions.push(p.x+radius*Math.cos(a),p.y,p.z+radius*Math.sin(a));}
  }
  for(let i=0;i<40;i++)for(let j=0;j<16;j++){const a=i*17+j,b=a+17;stemIndices.push(a,b,a+1,b,b+1,a+1);}
  const stemGeometry=new THREE.BufferGeometry();stemGeometry.setAttribute('position',new THREE.Float32BufferAttribute(stemPositions,3));stemGeometry.setIndex(stemIndices);stemGeometry.computeVertexNormals();
  for(const angle of [0,Math.PI/2,Math.PI,Math.PI*1.5])trace(t=>{const p=stem.getPoint(t),r=13-6*t+5*Math.exp(-Math.pow((t-.28)/.17,2));return p.add(new THREE.Vector3(r*Math.cos(angle),0,r*Math.sin(angle)));},.4,48);
  const cerebellum=new THREE.SphereGeometry(1,48,32);cerebellum.scale(55,35,55);cerebellum.translate(100,-65,0);
  const points=Array.from({length:850},(_,i)=>{
    const theta=Math.acos(1-2*(i+.5)/850), phi=(i*2.3999632297)%Math.PI;
    return brainSurface(theta,phi,i%2?1:-1);
  });
  return {lines,points,surfaces:[hemisphereGeometry(1),hemisphereGeometry(-1),cerebellum,stemGeometry]};
}
