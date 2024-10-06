import xml.etree.ElementTree as ET

# Tạo node gốc students
students = ET.Element("students")

# Tạo thông tin sinh viên 1
student1 = ET.SubElement(students, "student")
ET.SubElement(student1, "id").text = "123"
ET.SubElement(student1, "name").text = "Nguyễn Văn A"
ET.SubElement(student1, "birthYear").text = "2000"
ET.SubElement(student1, "class").text = "IT01"
ET.SubElement(student1, "gender").text = "Nam"

# Tạo thông tin sinh viên 2
student2 = ET.SubElement(students, "student")
ET.SubElement(student2, "id").text = "124"
ET.SubElement(student2, "name").text = "Trần Thị B"
ET.SubElement(student2, "birthYear").text = "1999"
ET.SubElement(student2, "class").text = "IT02"
ET.SubElement(student2, "gender").text = "Nữ"

# Tạo thông tin sinh viên 3
student3 = ET.SubElement(students, "student")
ET.SubElement(student3, "id").text = "125"
ET.SubElement(student3, "name").text = "Lê Văn C"
ET.SubElement(student3, "birthYear").text = "2001"
ET.SubElement(student3, "class").text = "IT03"
ET.SubElement(student3, "gender").text = "Nam"

# Tạo đối tượng ElementTree và ghi vào file XML
tree = ET.ElementTree(students)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)

# In ra màn hình (nếu muốn kiểm tra nội dung XML)
ET.dump(students)
