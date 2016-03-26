# -*- coding: utf-8 -*-
import os
import ast
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('type', help='What to parse?')
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




def printExpression(logLine):
    if logLine['severity'] != 'INFO':
        return

    logMessage = logLine['logMessage']
    if '{' not in logMessage:
        return

    try:
        logLineJson = ast.literal_eval(logMessage)
    except Exception as error:
        print logLine['logMessage']
        print error

    if 'type' in logLineJson:
        print logLineJson['expression'].encode('utf-8')





    logMessage = logLine['logMessage']
    if '{' not in logMessage:
        return

    try:
        logLineJson = ast.literal_eval(logMessage)
    except Exception as error:
        print logLine['logMessage']
        print error

    if 'message' in logLineJson and 'from' in logLineJson['message']:
        print logLineJson['message']['from']['id']




for fullLog in fullLogs:
    log = fullLog.get('protoPayload')
    if not log:
        continue

    if args.version and args.version != log['versionId']:
        continue

    for logLine in log.get('line', []):
        if args.type == 'expressions':
            printExpression(logLine)
