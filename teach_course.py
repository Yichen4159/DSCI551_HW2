import sys
from lxml import etree

iid, course_number, semester = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    tree = etree.parse("hw2.xml")
    root = tree.getroot()
except OSError:
    print("Error: Database does not exist")
    sys.exit()

# Check if instructor, course, and semester exist
if not root.xpath(f"instructors/instructor[@id='{iid}']") or not root.xpath(f"courses/course[@number='{course_number}' and @semester='{semester}']"):
    print("Error: Invalid input")
    sys.exit()

teach_courses = root.find("teach_courses")
if teach_courses is None:
    teach_courses = etree.SubElement(root, "teach_courses")

teach_course = etree.SubElement(teach_courses, "teach_course", instructor_id=iid, course_number=course_number, semester=semester)

tree = etree.ElementTree(root)
tree.write("hw2.xml", pretty_print=True)
