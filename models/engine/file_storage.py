#!/usr/bin/python3
'''new class'''
import os
import json


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
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                content = f.read()
                if len(content) != 0:
                    obj = json.loads(content)
                    for key, value in obj.items():
                        value = eval(value['__class__'])(**value)
                        FileStorage.new(self, value)

    def file_path():
        return FileStorage.__file_path
