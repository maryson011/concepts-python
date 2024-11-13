import urllib3
import json

def get(url):
    resp = urllib3.request('GET', url)
    return resp.data

def post(url, headers, payload):
    resposta = urllib3.request('POST', url, body=json.dumps(payload), headers=headers, timeout=100)
    data = resposta.data.decode('utf-8')
    return json.loads(data)