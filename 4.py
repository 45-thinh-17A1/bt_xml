from xml.dom.minidom import parse

# Tải file XML
doc = parse("sample.xml")

# In ra nội dung của tài liệu XML
print(doc.toprettyxml())
