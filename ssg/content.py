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
