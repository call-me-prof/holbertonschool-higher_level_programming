#!/usr/bin/env python3
"""
Module for serializing and deserializing data using XML format.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through the dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Write the XML tree to the specified file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        constructed_dict = {}
        for child in root:
            # Check if the text can be converted to an integer (like age)
            if child.text.isdigit():
                constructed_dict[child.tag] = int(child.text)
            else:
                constructed_dict[child.tag] = child.text

        return constructed_dict
    except Exception:
        return {}
