# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:25:40 2022

@author: Cameron Hill
"""


from typing import List
from pathlib import Path


class Parser():
    """ """
    extensions: List[str] = []

    def valid_extension(self,extension):
        """ """
        return extension in self.extensions

    def parse(self,path,source,dest):
        """ """
        raise NotImplementedError
