#! /usr/bin/python env

__author__ = 'dposlt'

#small script for school my daughter divmod

from gui import Screen

def getdiv():
    data = {20:2,40:2,32:3,132:5}

    for i in data:
        div = divmod(i, data[i])
        print(f'{i} : {data[i]} = {div[0]} zbytek {div[1]}')





guiScreen = Screen()
guiScreen.run()
