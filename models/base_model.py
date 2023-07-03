#!/usr/bin/python3
'''new class'''


from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        '''init func'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        cl_name = self.__class__.__name__
        return (f"[{cl_name}] ({self.id}) {self.__dict__}")

    def save(self):
        '''saving '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''dict'''
        new_dic = self.__dict__
        new_dic["__class__"] = self.__class__.__name__
        new_dic["created_at"] = new_dic["created_at"].isoformat()
        new_dic["updated_at"] = new_dic["updated_at"].isoformat()
        return new_dic
