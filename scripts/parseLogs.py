# -*- coding: utf-8 -*-
import os
import ast
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--version', '-v', help='Filter by version')
args = parser.parse_args()

statsDir = os.path.join(os.path.dirname(__file__), '..', 'stats')

fullLogs = []

for root, dirs, files in os.walk(statsDir):
    for filename in files:
        filepath = os.path.join(root, filename)
        with open(filepath, 'r') as file:
            for fullLogStr in file:
                fullLogs.append(json.loads(fullLogStr))


convertLogs = []

for fullLog in fullLogs:
    log = fullLog.get('protoPayload')
    if not log:
        continue

    if args.version and args.version != log['versionId']:
        continue

    for logLine in log.get('line', []):
        if logLine['severity'] != 'INFO':
            continue

        logMessage = logLine['logMessage']
        if '{' not in logMessage:
            continue

        try:
            logLineJson = ast.literal_eval(logMessage)
        except Exception as error:
            print logLine['logMessage']
            print error

        if 'type' in logLineJson:
            convertLogs.append(logLineJson)


for converLog in convertLogs:
    if converLog['type'] == 'success':
        continue

    print converLog['expression'].encode('utf-8')
