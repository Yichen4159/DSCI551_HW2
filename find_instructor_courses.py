import sys
from lxml import etree

# Get instructor id from command line argument
iid = sys.argv[1]

# Try to parse the existing XML file
try:
    tree = etree.parse("hw2.xml")
    root = tree.getroot()
except OSError:
    print("Error: Database does not exist")
    sys.exit()

# Find instructor and courses taught by the instructor
instructor = root.find(f"instructors/instructor[@id='{iid}']")
if instructor is None:
    print("Error: Instructor does not exist")
    sys.exit()

courses_taught = root.xpath(f"teach_courses/teach_course[@instructor_id='{iid}']")

# Create output XML
output_root = etree.Element("output")
output_instructor = etree.SubElement(output_root, "instructor", name=instructor.get("name"))

for course_taught in courses_taught:
    course_number = course_taught.get("course_number")
    semester = course_taught.get("semester")
    etree.SubElement(output_instructor, "course", number=course_number, semester=semester)

# Print output XML
print(etree.tostring(output_root, pretty_print=True).decode())
