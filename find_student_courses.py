import sys
from lxml import etree

# Get student id from command line argument
sid = sys.argv[1]

# Try to parse the existing XML file
try:
    tree = etree.parse("hw2.xml")
    root = tree.getroot()
except OSError:
    print("Error: Database does not exist")
    sys.exit()

# Find student and courses taken by the student
student = root.find(f"students/student[@id='{sid}']")
if student is None:
    print("Error: Student does not exist")
    sys.exit()

courses_taken = root.xpath(f"take_courses/take_course[@student_id='{sid}']")

# Create output XML
output_root = etree.Element("output")
output_student = etree.SubElement(output_root, "student", name=student.get("name"))

for course_taken in courses_taken:
    course_number = course_taken.get("course_number")
    semester = course_taken.get("semester")
    etree.SubElement(output_student, "course", number=course_number, semester=semester)

# Print output XML
print(etree.tostring(output_root, pretty_print=True).decode())
