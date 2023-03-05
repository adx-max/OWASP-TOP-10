print('XSS AUTO CHECKER FOR ALL PENETRATION TESTER, CREATED BY ANESTUS UDUME FROM BENTECH SECURITY')
import requests

url = 'https://example.com'

# Define the payload to inject
payload = '<script>alert("XSS");</script>'

# Define the input fields to test
input_fields = ['username', 'password', 'search']

# Loop through the input fields and test for XSS
for field in input_fields:
    # Send a POST request with the injected payload
    data = {field: payload}
    response = requests.post(url, data=data)

    # Check if the payload was reflected in the response
    if payload in response.text:
        print(f'XSS vulnerability found in input field: {field}')
