#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sys import argv
import os, io

global charset0, charset1, charset2, charset3, charDictionary, Built, charset
charset0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '%', '&', '/', '\\', '<', '>', '{', '}', '(', ')', '=', '"', "'", '+', '-', '*', '[', ']', '$', '|', '?', '-', '_', ' ']
charset1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
#Lowered the supported chars while testing to decrease dictionary building time.
charDictionary = {}
charset = []
Built = False

#Header: Charset integer + File end

def ReadHeader(file):
    if not(os.path.isfile(file)):
        return 0

    FileText = open(file,'r').read()
    

def BuildChar(charsetInt=0):
    try:
        int(charsetInt)
    except Exception as e:
        return e
    global charset0, charset1, charset2, charset3, charset, charDictionary, Built

    if(int(charsetInt) == 0):
        charset = charset0
    elif(int(charsetInt) == 1):
        charset = charset1
    elif(int(charsetInt) == 2):
        charset = charset2
    elif(int(charsetInt) == 3):
        charset = charset3
    else:
        return False

    for i in range(len(charset)):
        for y in range(len(charset)):
            charDictionary.update({"{}{}".format(charset[i], charset[y]):0})

    getList = list(charDictionary)
    for i in range(len(charDictionary)):
        charDictionary.update({getList[i]:chr(i+97)})
        if(i % 2 == 0):
            print("Building Charset {}%".format(str(round( i / len(charDictionary) * 100, 2 ))))

    Built = True

    

def Unpack():
    pass

def Pack(file):
    if not(Built):
        print("No charset built")
        return False
    if not(os.path.isfile(file)):
        print("File doesnt exist")
        return False
    global charDictionary, charset
    outText = ""
    encoded = ""
    inText = open(file,'r').read()

    for i in range(len(inText)):
        if inText[i] in charset:
            outText += inText[i]

    if len(outText) % 2 != 0:
        outText += ' '

    i=0
    while i<len(outText):
        try:
            encoded += charDictionary.get(outText[i]+outText[i+1])
        except Exception as e:
            print(e)
        i+=2

    #open(file+".ace",'w').write(encoded)
    io.open(file+".ace","w", encoding="utf-8").write(encoded)
    return True

BuildChar()
Pack("test.txt")

try:
    if(os.path.isfile(argv[1])):
        pass
except:
    pass
