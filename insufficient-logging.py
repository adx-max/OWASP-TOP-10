print('created by ANESTUS UDUME from BENTECH SECURITY')
import requests

# Define the URL of the login page
login_url = 'https://example.com/login'

# Define the credentials to use for the login attempt
username = 'user'
password = 'password'

# Set up a session with the web application
session = requests.Session()

# Send a request to the login page with the credentials
response = session.post(login_url, data={'username': username, 'password': password})

# Check the response to see if the login attempt was successful
if response.status_code == 200 and 'Invalid username or password' not in response.text:
    print('Successful login')

    # Define the URL of the monitoring page
    monitoring_url = 'https://example.com/monitoring'

    # Send a request to the monitoring page
    response = session.get(monitoring_url)

    # Check the response to see if the monitoring page is accessible
    if response.status_code == 200:
        print('Monitoring page accessible')
    else:
        print('Monitoring page not accessible')
else:
    print('Invalid credentials')
