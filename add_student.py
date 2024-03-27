import sys
from lxml import etree

sid, name, major = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    tree = etree.parse("hw2.xml")
    root = tree.getroot()
except OSError:
    root = etree.Element("root")

students = root.find("students")
if students is None:
    students = etree.SubElement(root, "students")

student = etree.SubElement(students, "student", id=sid, name=name, major=major)

tree = etree.ElementTree(root)
tree.write("hw2.xml", pretty_print=True)
