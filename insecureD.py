print'(CREATED BY ANESTUS UDUME FROM BENTECH SECURITY')
import requests
import pickle

# Define the URL of the web application
url = 'https://example.com/'

# Define the payload to send in the request
payload = {'data': 'test'}

# Serialize the payload using pickle
serialized_payload = pickle.dumps(payload)

# Define a list of HTTP methods to test (e.g. GET, POST, PUT, DELETE)
methods = ['GET', 'POST', 'PUT', 'DELETE']

# Loop through the methods to test each one
for method in methods:
    # Set up a session with the web application
    session = requests.Session()

    # Send a request to the web application with the serialized payload and current method
    response = session.request(method, url, data=serialized_payload)

    # Check the response to see if there are any signs of insecure deserialization
    if 'Traceback' in response.text:
        print(f'Insecure deserialization detected in response to {method} request')
