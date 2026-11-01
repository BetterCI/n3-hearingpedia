"""Cache primary/author/official sources for the foundational course; no recent SOTA claim."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,urllib.request,re
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/machine-learning/sources';OUT.mkdir(parents=True,exist_ok=True)
SOURCES={
'ml-generalization':'https://d2l.ai/chapter_linear-regression/generalization.html',
'ml-linear':'https://d2l.ai/chapter_linear-regression/linear-regression.html',
'ml-regularization':'https://d2l.ai/chapter_linear-regression/weight-decay.html',
'ml-softmax':'https://d2l.ai/chapter_linear-classification/softmax-regression.html',
'ml-shift':'https://d2l.ai/chapter_linear-classification/environment-and-distribution-shift.html',
'ml-mlp':'https://d2l.ai/chapter_multilayer-perceptrons/mlp.html',
'ml-backprop':'https://d2l.ai/chapter_multilayer-perceptrons/backprop.html',
'ml-cnn':'https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html',
'ml-leakage':'https://scikit-learn.org/stable/common_pitfalls.html',
'ml-cv':'https://scikit-learn.org/stable/modules/cross_validation.html',
'ml-metrics':'https://scikit-learn.org/stable/modules/model_evaluation.html',
'ml-calibration':'https://scikit-learn.org/stable/modules/calibration.html',
'ml-linear-api':'https://scikit-learn.org/stable/modules/linear_model.html',
'ml-pca':'https://scikit-learn.org/stable/modules/decomposition.html',
'ml-clustering':'https://scikit-learn.org/stable/modules/clustering.html',
'ml-svm':'https://scikit-learn.org/stable/modules/svm.html',
'ml-trees':'https://scikit-learn.org/stable/modules/tree.html',
'ml-ensembles':'https://scikit-learn.org/stable/modules/ensemble.html',
'ml-importance':'https://scikit-learn.org/stable/modules/permutation_importance.html',
'ml-wav2vec':'https://arxiv.org/abs/2006.11477',
'ml-hubert':'https://arxiv.org/abs/2106.07447',
'ml-attention':'https://arxiv.org/abs/1706.03762',
'ml-kapoor':'https://arxiv.org/abs/2207.07048',
'ml-kell':'https://pubmed.ncbi.nlm.nih.gov/29681533/',
'ml-attention-textbook':'https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html',
'ml-knn':'https://scikit-learn.org/stable/modules/neighbors.html',
'ml-optimization':'https://d2l.ai/chapter_optimization/sgd.html',
'ml-kapoor-published':'https://pubmed.ncbi.nlm.nih.gov/37720327/',
'ml-rl-policy':'https://d2l.ai/chapter_reinforcement-learning/value-iter.html',
'ml-wav2vec-published':'https://papers.nips.cc/paper_files/paper/2020/hash/92d1e1eb1cd6f9fba3227870bb6d7f07-Abstract.html',
'ml-rl':'https://d2l.ai/chapter_reinforcement-learning/mdp.html',
}
def fetch(item):
    key,url=item
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (Hearingpedia educational source check)'})
        with urllib.request.urlopen(req,timeout=40) as res: data=res.read();final=res.url
        suffix='.pdf' if data.startswith(b'%PDF') else '.html'
        (OUT/(key+suffix)).write_bytes(data)
        text=''
        if suffix=='.html':
            soup=BeautifulSoup(data,'html.parser')
            main=soup.select_one('article.bd-article') or soup.select_one('div.body') or soup.select_one('main') or soup
            for el in main.select('script,style,nav'):el.decompose()
            text=main.get_text('\n',strip=True)
            (OUT/(key+'.txt')).write_text(text,encoding='utf-8')
        blocked='Cookies must be enabled' in text and len(text)<1000
        return {'id':key,'url':url,'resolved_url':final,'status':'blocked-cookie-challenge' if blocked else 'fetched','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'text_characters':len(text),'cached_at':'2026-11-02'}
    except Exception as e:return {'id':key,'url':url,'status':'failed','error':str(e)}
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=7) as pool: rows=list(pool.map(fetch,SOURCES.items()))
    target=ROOT/'docs/research/machine-learning-2026-11-02/source-index.json'
    target.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for r in rows:print(r['id'],r['status'],r.get('text_characters',r.get('error')))
