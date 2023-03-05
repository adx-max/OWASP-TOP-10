print('created by ANESTUS UDUME FROM BENTECH SECURITY')
from zapv2 import ZAPv2

# Define the target URL of the web application to scan
target_url = 'http://localhost:8000'

# Define the API key to use for the ZAP API
api_key = 'apikey'

# Create a new ZAP instance and authenticate with the API key
zap = ZAPv2(apikey=api_key)

# Start a new spider scan on the target URL
zap.spider.scan(target_url)

# Wait for the spider scan to complete
while (int(zap.spider.status) < 100):
    print('Spider progress %: ' + zap.spider.status)
    time.sleep(1)

print('Spider completed')

# Start a new active scan on the target URL
zap.ascan.scan(target_url)

# Wait for the active scan to complete
while (int(zap.ascan.status) < 100):
    print('Active scan progress %: ' + zap.ascan.status)
    time.sleep(1)

print('Active scan completed')

# Get a list of security alerts detected by ZAP
alerts = zap.core.alerts()

# Check the alerts for any security issues
if len(alerts) > 0:
    print('Insecure web coding practices detected:')
    for alert in alerts:
        print(alert.get('name') + ': ' + alert.get('url'))
else:
    print('No insecure web coding practices found')
