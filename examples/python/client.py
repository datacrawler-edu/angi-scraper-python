"""Small integration helper: one paid start, SDK reads, verified completion."""
import csv
from datetime import timedelta
import json,os,sys,tempfile
from pathlib import Path
from urllib.request import Request,urlopen
from apify_client import ApifyClient

ACTOR_ID='datascraperes~angi-scraper'

def sdk(token,api_url='https://api.apify.com'):
    return ApifyClient(token,api_url=api_url,max_retries=1)

def start_and_wait(value,token=None,api_url='https://api.apify.com'):
    token=token or os.environ.get('APIFY_API_TOKEN')
    if not token:raise RuntimeError('Set APIFY_API_TOKEN before starting a run.')
    request=Request(api_url+'/v2/acts/'+ACTOR_ID+'/runs?timeout=180&maxTotalChargeUsd=0.05',data=json.dumps(value).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'},method='POST')
    try:
        with urlopen(request,timeout=30) as response:run_id=json.load(response)['data']['id']
    except Exception:
        raise RuntimeError('Start response unavailable. Inspect existing runs in Apify Console before trying again; this example will not start a second run automatically.') from None
    print('Run ID: '+run_id,file=sys.stderr)
    client=sdk(token,api_url)
    run=client.run(run_id).wait_for_finish(wait_duration=timedelta(seconds=240))
    if run is None or run.status!='SUCCEEDED':raise RuntimeError('Inspect run '+run_id+'; it did not finish successfully. Do not start another run automatically.')
    record=client.key_value_store(run.default_key_value_store_id).get_record('SUMMARY')
    summary=record['value'] if record else None
    if not isinstance(summary,dict) or summary.get('complete') is not True:
        raise RuntimeError('Run '+run_id+' has an incomplete or invalid-input summary. Inspect its log and saved results.')
    return client,run,summary

def dataset_rows(client,dataset_id,page_size=100):
    offset=0;seen=set()
    while True:
        page=client.dataset(dataset_id).list_items(offset=offset,limit=page_size,clean=False,desc=False)
        for row in page.items:
            key=row.get('recordId')
            if not key or key in seen:raise RuntimeError('Missing or duplicate record identity in export.')
            seen.add(key);yield row
        offset+=len(page.items)
        if len(page.items)<page_size:break

def collect(value,token=None,api_url='https://api.apify.com'):
    client,run,summary=start_and_wait(value,token,api_url)
    rows=list(dataset_rows(client,run.default_dataset_id))
    if len(rows)!=summary.get('deliveredRecords'):raise RuntimeError('Dataset count differs from SUMMARY; inspect the existing run.')
    return rows


def export_dataset(client,dataset_id,destination):
    """Export existing data atomically; never start another Actor run."""
    target=Path(destination);target.parent.mkdir(parents=True,exist_ok=True)
    handle=tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',newline='',dir=target.parent,prefix='.'+target.name,suffix='.tmp',delete=False)
    temporary=Path(handle.name);count=0
    try:
        with handle as output:
            fields=['recordId','recordType','proId','name','phone','zipCode','data']
            writer=csv.DictWriter(output,fieldnames=fields);writer.writeheader()
            for row in dataset_rows(client,dataset_id):
                data=row.get('data') or {}
                writer.writerow({'recordId':row['recordId'],'recordType':row['recordType'],'proId':data.get('proId'),'name':data.get('name'),'phone':data.get('phone'),'zipCode':data.get('zipCode') or (data.get('address') or {}).get('zip'),'data':json.dumps(data,ensure_ascii=False)})
                count+=1
        temporary.replace(target)
    except BaseException:
        temporary.unlink(missing_ok=True);raise
    return count
