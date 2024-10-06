import xml.etree.ElementTree as ET

# Tạo nút gốc company
company = ET.Element("company")

# Tạo các nút con và thêm dữ liệu vào
director_name = ET.SubElement(company, "directorName")
director_name.text = "Nguyễn Văn A"

address = ET.SubElement(company, "address")
address.text = "123 Đường ABC, Quận 1, TP. Hồ Chí Minh"

phone = ET.SubElement(company, "phone")
phone.text = "0123456789"

tax_code = ET.SubElement(company, "taxCode")
tax_code.text = "1234567890"

# Tạo đối tượng ElementTree và lưu vào file XML
tree = ET.ElementTree(company)
tree.write("company_info.xml", encoding="utf-8", xml_declaration=True)

# In ra màn hình (nếu muốn xem nội dung XML)
ET.dump(company)
