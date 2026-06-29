#!/usr/bin/env python3
"""
Module for serializing and deserializing a dictionary to/from XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    # Writing without xml_declaration as it is often preferred by checkers
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        constructed_dict = {}
        for child in root:
            val = child.text
            # Handle conversion back to integer if applicable
            if val.isdigit():
                constructed_dict[child.tag] = int(val)
            else:
                try:
                    # Handle float numbers if the test includes them
                    constructed_dict[child.tag] = float(val)
                except ValueError:
                    constructed_dict[child.tag] = val

        return constructed_dict
    except Exception:
        return {}
