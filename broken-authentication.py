print('script to check for broken authentication, created by ANESTUS UDUME from BENTECH SECURITY)
import requests

# Set the base URL of the website
base_url = "https://example.com"

# Define a list of common usernames and passwords to test
usernames = ['admin', 'root', 'test']
passwords = ['password', '123456', 'letmein']

# Loop through all combinations of usernames and passwords
for username in usernames:
    for password in passwords:
        # Send a POST request to the login page with the current credentials
        login_url = base_url + "/login"
        data = {'username': username, 'password': password}
        response = requests.post(login_url, data=data)

        # Check if the login was successful
        if response.status_code == 200 and "logout" in response.text.lower():
            print(f"Valid credentials found: {username}:{password}")
            break
        else:
            print(f"Invalid credentials: {username}:{password}")
