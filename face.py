import urllib,sys,urllib.request
import ssl


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=9fzN30jOQIq56RUHIeXnYGVB&client_secret=MMdG3ffbv5oh2TxD7Kw4ZH4EcaLiyrFk'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)





