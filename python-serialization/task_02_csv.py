#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and writes it to data.json in JSON format.
    Returns True if successful, or False if an exception occurs (e.g. file not found).
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # Use DictReader to automatically map rows to dictionaries
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        # Write the list of dictionaries to data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True
    except Exception:
        return False
