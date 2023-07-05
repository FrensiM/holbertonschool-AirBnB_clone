#!/usr/bin/python3
'''new class'''
import os
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''all func'''
        return FileStorage.__objects

    def new(self, obj):
        '''new func'''
        name_clas = self.__class__.__name__
        key = name_clas + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            new_dict = {}
            x = self.all()
            for element in x:
                new_dict[element] = x[element].to_dict()
            f.write(json.dumps(new_dict))
        return True

    def reload(self):
        my_dict = {'BaseModel': BaseModel}
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass

    def file_path():
        return FileStorage.__file_path
