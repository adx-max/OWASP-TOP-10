print('CREARED BY ANESTUS UDUME FROM BENTECH SECURITY, TO DETECT XXE VULN')
#!/usr/bin/python3

import lxml.etree as ET

# Define the XML file to check for XXE
xml_file = 'example.xml'

# Define a custom parser object with XXE protection enabled
parser = ET.XMLParser(no_network=True, dtd_validation=False)

# Parse the XML file with the custom parser object
try:
    tree = ET.parse(xml_file, parser=parser)
except ET.XMLSyntaxError as e:
    # If a syntax error is raised, check if it's caused by an XXE
    if 'DTD is prohibited' in str(e):
        print(f"XXE detected in file: {xml_file}")
    else:
        print(f"Error parsing file: {xml_file}, {e}")
