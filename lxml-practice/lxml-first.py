from lxml import etree


root = etree.Element("root", root_attr="someString")
child1 = etree.SubElement(root, "child1", ch_attr="some_ch")
child2 = root.append(etree.Element("child2"))
print(len(root))
print(root.get("root_attr"))
root.set("root_attr", "another")
root.set("hello", "Huhu")
root.text = "TEXT"
print(root.get("root_attr"))
print(etree.tostring(root, pretty_print=True))
print(sorted(root.keys()))

for name, value in sorted(root.items()):
    print(f'{name}, {value}')

attributes = root.attrib
print(attributes["hello"])


dict = {"key":"value"}

attributes["hello"] = "Guten Tag"
print(attributes["hello"])

print(root.get("hello"))
with open('open.txt', 'wb') as f:
    f.write(etree.tostring(root, pretty_print=True))
