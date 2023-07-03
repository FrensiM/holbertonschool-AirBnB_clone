#!/usr/bin/python3
'''new class'''


import os
import datetime
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name_clas = self.__class__.__name__
        key = name_clas + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        new_dic = {}
        for key in FileStorage.__objects:
            new_dic[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, encoding="utf-8", mode="w") as f:
            json.dump(new_dic, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="utf-8", mode="r") as f:
                for key, value in json.load(f).items():
                    value = eval(value["__class__"].items())
                    self.__objects[key] = value
        except:
            pass
