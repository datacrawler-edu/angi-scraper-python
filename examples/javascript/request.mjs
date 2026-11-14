import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';
export async function collect(input, {token=process.env.APIFY_API_TOKEN, base='https://api.apify.com', pause=ms=>new Promise(r=>setTimeout(r,ms))}={}) {
  if(!token)throw new Error('Set APIFY_API_TOKEN first.');
  async function request(path,options={}) {
    const response=await fetch(base+'/v2/'+path,{...options,headers:{Authorization:'Bearer '+token,'Content-Type':'application/json'},signal:AbortSignal.timeout(30000)});
    if(!response.ok)throw new Error('Apify request failed; inspect the existing run before restarting.');
    const body=await response.json();return body?.data??body;
  }
  // Exactly one POST. A lost start response must be reconciled in Console.
  const started=await request('acts/datascraperes~angi-scraper/runs?timeout=180&maxTotalChargeUsd=0.05',{method:'POST',body:JSON.stringify(input)});
  console.error('Run ID: '+started.id);
  const deadline=Date.now()+240000;let run;
  while(Date.now()<deadline){
    run=await request('actor-runs/'+started.id);
    if(['SUCCEEDED','FAILED','ABORTED','TIMED-OUT'].includes(run.status))break;
    await pause(2000);
  }
  if(run?.status!=='SUCCEEDED')throw new Error('Existing run did not succeed; inspect '+started.id);
  const summary=await request('key-value-stores/'+run.defaultKeyValueStoreId+'/records/SUMMARY');
  if(summary.complete!==true)throw new Error('Inspect incomplete/invalid-input SUMMARY for '+started.id);
  const rows=[],seen=new Set();let offset=0;
  while(true){
    const page=await request('datasets/'+run.defaultDatasetId+'/items?clean=false&desc=false&limit=100&offset='+offset);
    for(const row of page){if(!row.recordId||seen.has(row.recordId))throw new Error('Missing or duplicate record identity.');seen.add(row.recordId);rows.push(row);}
    offset+=page.length;if(page.length<100)break;
  }
  if(rows.length!==summary.deliveredRecords)throw new Error('Dataset count differs from SUMMARY.');
  return rows;
}
if(process.argv[1]&&fileURLToPath(import.meta.url)===resolve(process.argv[1])) {
  const input=JSON.parse(await readFile(new URL('../../data/sample-input.json',import.meta.url),'utf8'));
  console.log(JSON.stringify(await collect(input),null,2));
}
