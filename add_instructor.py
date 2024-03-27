import sys
from lxml import etree

iid, name, department = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    tree = etree.parse("hw2.xml")
    root = tree.getroot()
except OSError:
    root = etree.Element("root")

instructors = root.find("instructors")
if instructors is None:
    instructors = etree.SubElement(root, "instructors")

instructor = etree.SubElement(instructors, "instructor", id=iid, name=name, department=department)

tree = etree.ElementTree(root)
tree.write("hw2.xml", pretty_print=True)
