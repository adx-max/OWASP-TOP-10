print('CREATED BY ANESTUS UDUME, FROM BENTECH SECURITY')
import requests

# Define the URL of the web page to test
url = 'https://example.com/'

# Define a list of headers to test for security misconfigurations
headers = ['Server', 'X-Powered-By', 'X-AspNet-Version', 'X-AspNetMvc-Version', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy', 'Strict-Transport-Security']

# Define a list of HTTP methods to test (e.g. GET, POST, PUT, DELETE)
methods = ['GET', 'POST', 'PUT', 'DELETE']

# Loop through the headers and methods to test each combination
for header in headers:
    for method in methods:
        # Set up a session with the web page
        session = requests.Session()

        # Send a request to the web page with the current method and header
        response = session.request(method, url, headers={header: 'test'})

        # Check the response headers to see if the header is reflected
        if header in response.headers:
            print(f'{header} header is reflected in response to {method} request')
