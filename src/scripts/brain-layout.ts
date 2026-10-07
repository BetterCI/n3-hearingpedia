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

export function brainNodePositions(count:number, cortexCandidates?:THREE.Vector3[]) {
  const positions:THREE.Vector3[]=[];
  if(cortexCandidates?.length) {
    const candidates=[cortexCandidates.filter(p=>p.z>0),cortexCandidates.filter(p=>p.z<0)];
    const scores=candidates.map(hemisphere=>hemisphere.map(()=>Infinity));
    for(let i=0;i<count;i++) {
      const side=i%2, pool=candidates[side];let best=0;
      if(i===0)best=pool.reduce((winner,p,j)=>p.x<pool[winner].x?j:winner,0);
      else for(let j=1;j<pool.length;j++)if(scores[side][j]>scores[side][best])best=j;
      const p=pool[best].clone();positions.push(p);
      candidates.forEach((hemisphere,s)=>hemisphere.forEach((q,j)=>{
        const projected=(q.x-p.x)**2+(q.y-p.y)**2;
        const distance=p.distanceToSquared(q);
        scores[s][j]=Math.min(scores[s][j],s===side?distance:Math.min(distance,projected*1.44+28**2));
      }));
    }
    return positions;
  }
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

interface CortexAsset {version:number;positionScale:number;sulcScale:number;hemispheres:{side:string;positions:number[];triangles:number[];sulc:number[]}[];}

/** Load from this website, with the procedural silhouette available offline. */
export async function loadBrainScaffold(source:string) {
  try {
    const response=await fetch(source,{signal:AbortSignal.timeout(6000)});
    if(!response.ok)throw new Error('Cortex unavailable');
    const asset:CortexAsset=await response.json();
    if(asset.version!==1||asset.hemispheres.length!==2)throw new Error('Invalid cortex');
    const all=asset.hemispheres.flatMap(h=>h.positions);
    const min=[Infinity,Infinity,Infinity],max=[-Infinity,-Infinity,-Infinity];
    for(let i=0;i<all.length;i++){min[i%3]=Math.min(min[i%3],all[i]);max[i%3]=Math.max(max[i%3],all[i]);}
    const scale=310/(max[1]-min[1]),center=min.map((v,i)=>(v+max[i])/2);
    const surfaces:THREE.BufferGeometry[]=[],candidates:THREE.Vector3[]=[],points:THREE.Vector3[]=[];
    for(const hemi of asset.hemispheres) {
      const positions:number[]=[],colors:number[]=[];
      const side=hemi.side==='left'?-1:1;
      for(let i=0;i<hemi.positions.length;i+=3) {
        const p=new THREE.Vector3(-(hemi.positions[i+1]-center[1])*scale,(hemi.positions[i+2]-center[2])*scale+18,(hemi.positions[i]-center[0])*scale+side*3);
        positions.push(p.x,p.y,p.z);
        const light=THREE.MathUtils.clamp(.5-hemi.sulc[i/3]*asset.sulcScale*.25,0,1);
        colors.push(.025+light*.035,.045+light*.045,.07+light*.06);
        if(i%18===0)points.push(p.clone());
        if(i%9===0&&Math.abs(p.z)>17&&light>.35)candidates.push(new THREE.Vector3(p.x*1.055,(p.y-18)*1.055+18,p.z*1.055));
      }
      const indices:number[]=[];
      // Swapping the display axes reverses handedness.
      for(let i=0;i<hemi.triangles.length;i+=3)indices.push(hemi.triangles[i],hemi.triangles[i+2],hemi.triangles[i+1]);
      const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.Float32BufferAttribute(positions,3));geometry.setAttribute('color',new THREE.Float32BufferAttribute(colors,3));geometry.setIndex(indices);geometry.computeVertexNormals();surfaces.push(geometry);
    }
    return {surfaces,points,candidates,lines:[] as {points:THREE.Vector3[];opacity:number}[],anatomical:true};
  } catch {
    // The same graph remains usable when the extra shape asset cannot load.
    const fallback=createBrainScaffold();
    return {...fallback,candidates:undefined,anatomical:false};
  }
}

export function createBrainScaffold() {
  // Lightweight local fallback when the cortical mesh is unavailable.
  const lines:{points:THREE.Vector3[];opacity:number}[]=[];
  for(const side of [-1,1])for(const phi of [0,Math.PI*.3,Math.PI*.65,Math.PI]) {
    lines.push({points:Array.from({length:81},(_,i)=>brainSurface(i/80*Math.PI,phi,side)),opacity:.14});
  }
  const points=Array.from({length:850},(_,i)=>brainSurface(Math.acos(1-2*(i+.5)/850),(i*2.3999632297)%Math.PI,i%2?1:-1));
  return {lines,points,surfaces:[hemisphereGeometry(1),hemisphereGeometry(-1)]};
}
