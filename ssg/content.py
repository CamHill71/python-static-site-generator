# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:25:40 2022

@author: Cameron Hill
"""


import re

from yaml import load,FullLoader

from collections.abc import Mapping


class Content(Mapping):
    """"""
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter,re.MULTILINE)

    @classmethod
    def load(cls,string):
        """ """
        _,fm,content = cls.__regex.split(string,2)

        metadata = load(fm,Loader=FullLoader)

        return cls(metadata,content)

    def __init__(self,metadata,content) -> None:
        """"""
        self.data = metadata
        self.data["content"] = content
        
    @property
    def body(self):
        """ """
        return self.data["content"]

    @property
    def type(self):
        """ """   
        return self.data["type"] if "type"  in self.data else None 

    @type.setter
    def type(self,type):
        """ """
        self.data["type"] = type

    def __getitem__(self,key):
        """ """
        return self.data[key]

    def __len__(self):
        """ """
        return len(self.data)

    def __repr__(self) -> str:
        data = {}

        for key,value in self.data.items():
            if key != "content":
                data[key] = value

        return str(data)  

    def __iter__(self):
        """"""
        self.data.__iter__()