#!/usr/bin/env python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """
    A custom class that represents a student object.
    """
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes the CustomObject with name, age, and student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints out the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object and saves it to a file.
        Returns None if an exception occurs.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from the provided file.
        Returns None if the file does not exist or is malformed.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
