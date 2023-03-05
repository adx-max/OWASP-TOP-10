print('CREATED BY ANESTUS UDUME FROM BENTECH SECURITY')
import subprocess

# Define the path to your project's requirements file
requirements_file_path = 'requirements.txt'

# Define the command to run the Safety tool
command = f'safety check -r {requirements_file_path}'

# Run the command and capture the output
output = subprocess.check_output(command, shell=True)

# Decode the output as a string
output_str = output.decode('utf-8')

# Check the output for any vulnerabilities
if 'No known vulnerabilities found' not in output_str:
    print('Components with known vulnerabilities detected:')
    print(output_str)
else:
    print('No components with known vulnerabilities found')
