"""Export the completed study to static JSON, without service credentials or runtime files.
Usage: python3 scripts/export-study.py /path/to/olens_motivated_reasoning_run
"""
import hashlib, json, sys
from pathlib import Path

root=Path(sys.argv[1]).resolve()
public=Path(__file__).resolve().parents[1]/'public'
data=public/'data'
(data/'records').mkdir(parents=True,exist_ok=True)
(data/'analysis').mkdir(parents=True,exist_ok=True)
read=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
readings={}
for p in sorted((root/'mirror/readouts').glob('*.json')):
 r=read(p);readings.setdefault(r['activation_id'],[]).append(r)
rows=[];unique_readouts=set();activation_ids=set();raw_hashes={}
for job in read(root/'jobs.json'):
 p=root/'mirror/results'/f"{job['id']}.json"
 r=read(p);r.pop('full_ids',None)
 raw_hashes['results/'+p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
 for site in r.get('sites',[]):
  for cell in site['layers']:
   aid=cell['activation_id'];activation_ids.add(aid)
   cell['readouts']=sorted(readings.get(aid,[]),key=lambda x:x['role'])
   for reading in cell['readouts']:unique_readouts.add((aid,reading['role']))
 r['readouts_count']=sum(len(c['readouts']) for s in r.get('sites',[]) for c in s['layers'])
 if job['kind']=='excerpt':r['title']=job.get('case_id','')+' · '+job.get('anchor','')
 write(data/'records'/p.name,r)
 rows.append({k:r.get(k) for k in ['id','family','kind','condition','thinking','replicate','status','readouts_count','title']})
assert len(rows)==787 and len(unique_readouts)==3258 and len(activation_ids)==2056
for name in ['assessment','completeness','numeric_results']:
 write(data/'analysis'/f'{name}.json',read(root/'analysis'/f'{name}.json'))
write(data/'analysis/protocol.json',read(root/'protocol.json'))
write(data/'index.json',dict(updated=read(root/'analysis/assessment.json')['updated'],phase='complete',message='Completed study. Static archive.',counts=dict(subject_done=740,subject_total=740,readouts_done=3258,readouts_planned=3258,diagnostic_contexts_done=47),eta='Complete',workers=[],records=rows))
report=(root/'FINAL_REPORT.md').read_text().replace('https://qwen-olens-study.therealgasty.chatgpt.site/','https://agastyasridharan.github.io/qwen-olens-study/')
(public/'FINAL_REPORT.md').write_text(report)
for p in sorted((root/'mirror/readouts').glob('*.json')):raw_hashes['readouts/'+p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
write(data/'provenance.json',dict(source_ui_commit='9e3316723bbcc2f7a06bd251a77ec53d50fda4a2',records=len(rows),unique_readouts=len(unique_readouts),activations=len(activation_ids),source_report_sha256=hashlib.sha256((root/'FINAL_REPORT.md').read_bytes()).hexdigest(),report_change='Dashboard links changed to GitHub Pages; scientific text unchanged.',raw_file_sha256=raw_hashes))
print(f'Exported {len(rows)} records, {len(unique_readouts)} unique readouts, {len(activation_ids)} activations.')
