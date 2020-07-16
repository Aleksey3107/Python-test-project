import json
import requests
import ast

HEADERS = {'access-control-allow-headers', 'access-control-allow-methods', 'access-control-allow-origin',
           'content-type', 'date', 'server', 'content-length', 'connection', 'matched-stub-id', 'matched-stub-name',
           'content-encoding', 'vary', 'transfer-encoding'}

host = 'http://192.168.10.20:1341'
url = '/v2/fast-match/teasers'
request_parameters = {
    'locale': 'en'
}

response = requests.get(host + url, params=request_parameters)



def process_headers(response, header):
    response_headers = response.headers
    if header in response_headers:
        return f'{header}: {response_headers[header]}'
    else:
        return None


for header in HEADERS:
    process_headers(response, header)

# print(process_headers(send_request(host=host, url=url, params=request_parameters)))
