# -*- coding: utf-8 -*-
"""Convertit le JSON 01_user en XML exploitable par TreeSheet (structure hiérarchique)."""
import json
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

def sanitize_tag(name):
    """Nom de balise XML valide (alphanum + underscore)."""
    s = re.sub(r'[^\w\-]', '_', str(name))
    return s if s and s[0].isalpha() else 'n_' + s

def dict_to_xml(parent, data, tag_name="item"):
    """Convertit dict/liste/valeur en éléments XML sous parent."""
    if data is None:
        parent.set("nil", "true")
        return
    if isinstance(data, bool):
        parent.text = "true" if data else "false"
        return
    if isinstance(data, (int, float)):
        parent.text = str(data)
        return
    if isinstance(data, str):
        parent.text = data
        return
    if isinstance(data, list):
        for i, item in enumerate(data):
            child = ET.SubElement(parent, "item")
            if isinstance(item, dict):
                for k, v in item.items():
                    sub = ET.SubElement(child, sanitize_tag(k))
                    dict_to_xml(sub, v, k)
            else:
                dict_to_xml(child, item, "item")
        return
    if isinstance(data, dict):
        for k, v in data.items():
            child = ET.SubElement(parent, sanitize_tag(k))
            dict_to_xml(child, v, k)
        return

def main():
    import os
    base = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base, "01_user_9800552_2026-02-04_13-55_9800552_00338243.json")
    xml_path = os.path.join(base, "01_user_9800552_2026-02-04_13-55_9800552_00338243.xml")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    root = ET.Element("recap")
    dict_to_xml(root, data, "recap")

    tree = ET.ElementTree(root)
    rough = ET.tostring(root, encoding="unicode", method="xml")
    dom = minidom.parseString(rough)
    pretty = dom.toprettyxml(indent="  ", encoding=None)

    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(pretty)

    print("XML écrit:", xml_path)

if __name__ == "__main__":
    main()
