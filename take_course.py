import sys
from lxml import etree

sid, course_number, semester = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    tree = etree.parse("hw2.xml")
    root = tree.getroot()
except OSError:
    print("Error: Database does not exist")
    sys.exit()

# Check if student, course, and semester exist
if not root.xpath(f"students/student[@id='{sid}']") or not root.xpath(f"courses/course[@number='{course_number}' and @semester='{semester}']"):
    print("Error: Invalid input")
    sys.exit()

take_courses = root.find("take_courses")
if take_courses is None:
    take_courses = etree.SubElement(root, "take_courses")

take_course = etree.SubElement(take_courses, "take_course", student_id=sid, course_number=course_number, semester=semester)

tree = etree.ElementTree(root)
tree.write("hw2.xml", pretty_print=True)
