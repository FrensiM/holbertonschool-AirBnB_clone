#!/usr/bin/python3
'''new class'''


import os
import datetime
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
        new_dic = {}
        for key in FileStorage.__objects:
            new_dic[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, encoding="utf-8", mode="w") as f:
            json.dump(new_dic, f)

    def reload(self):
       if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                try:
                    self.__objects = json.load(file)
                except json.JSONDecodeError:
                    pass