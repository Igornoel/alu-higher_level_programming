#!/usr/bin/python3
import json
from os import path
from models.rectangle import Rectangle
from models.square import Square

class Base:
    @classmethod
    def from_json_string(cls, json_string):
        """Converts a JSON string into a list of objects."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with the provided dictionary."""
        if cls.__name__ == 'Rectangle':
            return Rectangle(**dictionary)
        elif cls.__name__ == 'Square':
            return Square(**dictionary)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file."""
        filename = f"{cls.__name__}.json"
        
        # Check if the file exists
        if not path.exists(filename):
            return []
        
        # Open the file and read its content
        with open(filename, "r") as file:
            json_string = file.read()
        
        # If the file is empty or contains "[]", return an empty list
        if json_string == "[]":
            return []
        
        # Convert the JSON string to a list of dictionaries
        list_of_dicts = cls.from_json_string(json_string)
        
        # Create instances based on the dictionary and return them
        return [cls.create(**item) for item in list_of_dicts]
