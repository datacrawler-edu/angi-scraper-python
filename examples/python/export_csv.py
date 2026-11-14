"""Export an existing Dataset without starting or rerunning the Actor."""
import argparse,os
from client import sdk,export_dataset

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('dataset_id');parser.add_argument('--output',default='data/exported-angi.csv');args=parser.parse_args()
    token=os.environ.get('APIFY_API_TOKEN')
    if not token:raise SystemExit('Set APIFY_API_TOKEN to read your Dataset.')
    count=export_dataset(sdk(token),args.dataset_id,args.output);print(f'Exported {count} rows to {args.output}')

if __name__=='__main__':main()
