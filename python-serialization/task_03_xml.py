#!/usr/bin/env python3
"""
This module provides functions to serialize a dictionary into an XML file
and deserialize an XML file back into a Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary and saves it as an XML file.

    Args:
        dictionary (dict): The dictionary containing data to serialize.
        filename (str): The target XML file name.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads an XML file and converts it back into a Python dictionary.

    Args:
        filename (str): The XML file to read and deserialize.

    Returns:
        dict: The reconstructed dictionary from XML data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        constructed_dict = {}
        for child in root:
            if child.text.isdigit():
                constructed_dict[child.tag] = int(child.text)
            else:
                constructed_dict[child.tag] = child.text

        return constructed_dict
    except Exception:
        return {}
