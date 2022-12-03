#!/usr/bin/python3

def uppercase(str):
    uppercase = __import__('8-uppercase').uppercase
    uppercase("Holberton School")
    print("{}{}".format(uppercase.upper()))
    uppercase("Holberon School, 98 Battery street")
    print("{}{}, {}{}{}".format(uppercase.upper()))
