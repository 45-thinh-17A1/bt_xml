from xml.dom.minidom import parse

# Tải file XML
doc = parse("sample.xml")

# Lấy danh sách các phần tử <name> trong file XML
names = doc.getElementsByTagName("name")

# In ra tên của từng phần tử
for name in names:
    print(name.firstChild.data)
