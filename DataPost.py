import base64
import json
import urllib.request

# 変数は必要に応じて外部化してください。
url = "http://localhost:8000/api/Log_datas/"
method = "POST"
headers = {"Content-Type": "application/json", }

user = "kaoru"
password = "yukanya"

s_matt_id = 4
weight = 10.2
quantity = 2

# PythonオブジェクトをJSONに変換する
obj = {"s_matt_id": s_matt_id, "weight": weight, "quantity": quantity, }
json_data = json.dumps(obj).encode("utf-8")

credentials = ('%s:%s' % (user, password))
encoded_credentials = base64.b64encode(credentials.encode('ascii'))

# httpリクエストを準備してPOST
request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
request.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

with urllib.request.urlopen(request) as response:
    response_body = response.read().decode("utf-8")