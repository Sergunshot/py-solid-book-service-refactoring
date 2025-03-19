import json
import xml.etree.ElementTree as ET


class ConvertJson:
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})

    def __call__(self, *args, **kwargs):
        return self.serialize(*args, **kwargs)


class ConvertXml:
    def serialize(self, book_title: str, book_content: str) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book_title
        content = ET.SubElement(root, "content")
        content.text = book_content
        return ET.tostring(root, encoding="unicode")

    def __call__(self, *args, **kwargs):
        return self.serialize(*args, **kwargs)
