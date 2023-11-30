import xml.etree.cElementTree as ET

file_xml = ET.parse('file.xml')
root = file_xml.getroot()

for element in root.iter():
    print(element.tag, element.attrib, element.text)