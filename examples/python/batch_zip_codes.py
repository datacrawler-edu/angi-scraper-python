"""One bounded hosted run per distinct ZIP; stop on incomplete collection."""
import argparse,json,re
from client import collect

def batch(zip_codes,query='Plumbing',token=None,api_url='https://api.apify.com'):
    codes=list(dict.fromkeys(zip_codes))
    if not codes or any(not isinstance(code,str) or not re.fullmatch('[0-9]{5}',code) for code in codes):
        raise ValueError('Provide five-digit US ZIP codes before starting any run.')
    records={}
    for code in codes:
        for row in collect({'mode':'pros','query':query,'zipCode':code,'maxItems':2},token,api_url):
            records.setdefault(row['recordId'],row)
    return list(records.values())

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('zip_codes',nargs='+');parser.add_argument('--service',default='Plumbing');args=parser.parse_args()
    print(json.dumps(batch(args.zip_codes,args.service),indent=2,ensure_ascii=False))

if __name__=='__main__':main()
