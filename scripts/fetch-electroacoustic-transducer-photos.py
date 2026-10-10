"""Copy openly licensed originals into website assets without image alteration."""
from pathlib import Path
import requests, json, hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'public/figures/electroacoustic-transducer';OUT.mkdir(parents=True,exist_ok=True)
photos=[
{'file':'photo-moving-coil.jpg','source':'https://commons.wikimedia.org/wiki/File:Lautsprecher_Aufbau.jpg','creator':'Patrick.Nordmann','license':'CC BY-SA 4.0','license_url':'https://creativecommons.org/licenses/by-sa/4.0/','description':'拆开的扬声器：照片可见磁体、音圈与振膜。','label':'a．动圈扬声器的拆解'},
{'file':'photo-electret.jpg','source':'https://commons.wikimedia.org/wiki/File:Electret_microphone_MKE3.JPG','creator':'Kae','license':'CC BY-SA 3.0','license_url':'https://creativecommons.org/licenses/by-sa/3.0/','description':'左为MKE-3驻极体敏感胶囊，右为含缓冲放大器的完整麦克风组件。','label':'b．驻极体胶囊与完整组件'},
{'file':'photo-mems-microphone.jpg','source':'https://commons.wikimedia.org/wiki/File:Asus_Zenbook_UX32V_-_webcam_module_-_AK230_0539L_4911C-0108.jpg','creator':'Raimond Spekking','license':'CC BY-SA 4.0','license_url':'https://creativecommons.org/licenses/by-sa/4.0/','description':'电路板上的Akustica AKU230 CMOS MEMS数字麦克风封装；内部敏感结构不可见。','label':'c．MEMS数字麦克风封装'},
{'file':'photo-piezo.jpg','source':'https://commons.wikimedia.org/wiki/File:2007-07-24_Piezoelectric_buzzer.jpg','creator':'Gophi','license':'CC BY-SA 3.0','license_url':'https://creativecommons.org/licenses/by-sa/3.0/','description':'蜂鸣器中的金属圆片与压电片；用于观察压电结构，不代表宽带音频扬声器性能。','label':'d．压电声输出元件'},
]
originals={
'photo-moving-coil.jpg':'https://upload.wikimedia.org/wikipedia/commons/4/4d/Lautsprecher_Aufbau.jpg',
'photo-electret.jpg':'https://upload.wikimedia.org/wikipedia/commons/6/67/Electret_microphone_MKE3.JPG',
'photo-mems-microphone.jpg':'https://upload.wikimedia.org/wikipedia/commons/6/67/Asus_Zenbook_UX32V_-_webcam_module_-_AK230_0539L_4911C-0108.jpg',
'photo-piezo.jpg':'https://upload.wikimedia.org/wikipedia/commons/d/d3/2007-07-24_Piezoelectric_buzzer.jpg',
}
# Original URLs were resolved from the source pages' original-file links with web tools.
session=requests.Session();session.headers['User-Agent']='Hearingpedia/1.0 (https://github.com/betterci/n3-hearingpedia; educational image attribution) python-requests/2.32'
for r in photos:
    dest=OUT/r['file']
    if dest.exists():
        old=json.loads((OUT/'photo-credits.json').read_text(encoding='utf-8'))
        r.update(next(x for x in old if x['file']==r['file']));continue
    url=originals[r['file']];response=session.get(url,timeout=45);response.raise_for_status()
    assert response.headers.get('Content-Type','').startswith('image/jpeg')
    dest.write_bytes(response.content)
    r.update(original_url=url,sha256=hashlib.sha256(response.content).hexdigest(),bytes=len(response.content),retrieved_at='2026-10-10',alteration='None: original file bytes copied; display scaled with CSS',role='Illustrative photograph, not comparative performance evidence')
    # Persist after each success so an interrupted retrieval can resume safely.
    (OUT/'photo-credits.json').write_text(json.dumps([x for x in photos if 'sha256' in x],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(r['file'],len(response.content))
(OUT/'photo-credits.json').write_text(json.dumps(photos,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rows=['<figure>','  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:22px;align-items:start;">']
for r in photos:
    credit=('© ' if r['creator']=='Raimond Spekking' else '')+r['creator']
    rows +=['    <div>',f'      <img src="/n3-hearingpedia/figures/electroacoustic-transducer/{r["file"]}" alt="{r["description"]}" loading="lazy" style="width:100%;height:250px;object-fit:contain;background:#f5f7f8;" />',f'      <p style="font-size:14px;line-height:1.65;"><strong>{r["label"]}</strong>。{r["description"]}</p>',f'      <p style="font-size:12px;line-height:1.6;">{credit} / <a href="{r["license_url"]}">{r["license"]}</a> (via Wikimedia Commons) · <a href="{r["source"]}">原图与来源</a> · 原图未修改。</p>','    </div>']
rows +=['  </div>','  <figcaption>图 2．四类器件的实物例子。照片按各自原始许可使用，完整保留原图，仅在页面中缩放显示；各图不是同一比例尺。外形和可见结构帮助识别器件，不能据照片判断带宽、灵敏度或音质。封装照片也不能直接展示MEMS内部工作机制。</figcaption>','</figure>']
path=ROOT/'src/content/concepts/electroacoustic-transducer.md';s=path.read_text(encoding='utf-8')
if 'photo-moving-coil.jpg' not in s:
    # Renumber existing figures and textual references before inserting the new gallery.
    for old,new in [('图 4','图 5'),('图 3','图 4'),('图 2','图 3')]:s=s.replace(old,new)
    s=s.replace('### MEMS 是制造与集成框架','### 从实物观察结构与封装\n\n图 2 把用途、机制与封装分开呈现：扬声器拆解展示运动结构；驻极体例子区分敏感胶囊和电子组件；MEMS照片展示封装与板级连接；压电圆片展示另一种执行结构。观察实物时，应把照片能显示的部件与需要原理图或测量才能判断的性质分开。\n\n'+'\n'.join(rows)+'\n\n### MEMS 是制造与集成框架',1)
    path.write_text(s,encoding='utf-8')
print('Four credited original photographs added.')
