import argparse
import os
import tempfile
import json

def create_parser():
    pars = argparse.ArgumentParser()
    pars.add_argument('--key')
    pars.add_argument('--val')
    return pars

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser = create_parser()
if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        pass
with open(storage_path, 'r') as f:
    if (f.read()):
        f.seek(0)
        keyDict = json.load(f)
    else:
        keyDict = dict()
parser = parser.parse_args()
if parser.key and parser.val:
    if parser.key in keyDict:
        keyDict[parser.key].append(parser.val)
    else:
        keyDict[parser.key] = list()
        keyDict[parser.key].append(parser.val)
elif parser.key and (parser.key in keyDict):
    print(*keyDict[parser.key], sep=', ')
if len(keyDict):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(keyDict))