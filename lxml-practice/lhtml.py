from lxml import etree

root = etree.Element("root")
print(root.tag)
root.append(etree.Element("child1"))
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")
print(etree.tostring(root, pretty_print=True))

child = root[0]
print(child.tag)

print(len(root))

print(root.index(root[1]))

children = list(root)

for child in children:
    print(child.tag)

for child in root:
    print(child.tag)

root.insert(0, etree.Element("child0"))

start = root[:1]
end = root[-1:]

print(start)

print(start[0].tag)

print(etree.iselement(root))

if len(root):
    print("root have at least 1 child")

html = etree.Element("html")
head = etree.SubElement(html, "head")
title = etree.SubElement(head, "title")
title.text = "My html"
meta = etree.SubElement(head, "meta", charset="UTF-8")
body = etree.SubElement(html, "body")
h1 = etree.SubElement(body, "h1")
h1.text = "This is "
strong = etree.SubElement(h1, "strong")
strong.text = "HEADING"
strong.tail = "example"
ins = etree.SubElement(h1, "ins")
ins.text = "Get it !?"
ins.tail = "or not ?"
with open('open.txt', 'wb') as f:
    f.write(etree.tostring(html, pretty_print=True, method="XML"))

for elem in html.iter():
    print(elem.tag)

with open('some.xml', 'rb+') as f:
    a = etree.parse(f)
    print(etree.tostring(a, encoding="windows-1251"))
    f.write(etree.tostring(a, encoding="windows-1251"))
