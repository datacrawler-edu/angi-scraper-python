"""Run the hosted Angi Actor with a small supplied example input."""
import json
from pathlib import Path
from client import collect

def main():
    value=json.loads((Path(__file__).resolve().parents[2]/'data/sample-input.json').read_text(encoding='utf-8'))
    print(json.dumps(collect(value),indent=2,ensure_ascii=False))

if __name__=='__main__':main()
