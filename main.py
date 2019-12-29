#! /env/src/python env

__author__ = 'dposlt'

#small script for school my daughter divmod

def getdiv():
    data = {20:2,40:2,32:3,132:5}

    for i in data:
        div = divmod(i, data[i])
        print(f'{i} : {data[i]} = {div[0]} zbytek {div[1]}')




print(getdiv())
