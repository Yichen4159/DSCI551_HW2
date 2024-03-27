import sys
from lxml import etree

course_number, course_name, semester = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    tree = etree.parse("hw2.xml")
    root = tree.getroot()
except OSError:
    root = etree.Element("root")

courses = root.find("courses")
if courses is None:
    courses = etree.SubElement(root, "courses")

course = etree.SubElement(courses, "course", number=course_number, name=course_name, semester=semester)

tree = etree.ElementTree(root)
tree.write("hw2.xml", pretty_print=True)
