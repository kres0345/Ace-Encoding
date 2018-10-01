#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from itertools import combinations
global dictionaryChar, chars2
dictionaryChar = {}
chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']

def __init__():
    global dictionaryChar, chars2
    #chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '%', '&', '/', '\\', '<', '>', '{', '}', '(', ')', '=', '"', "'", '+', '-', '*', '[', ']', '$', '|', '?', '-', '_', ' ']
    #chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
    #Lowered the supported chars while testing to decrease dictionary building time.

    #chars = []
    #dictionaryChar = {}


    i=0
    while(i<len(chars2)):
        y=0
        while(y<len(chars2)):
            dictionaryChar.update({"{}{}".format(chars2[i],chars2[y]):0})
            #print("{}{}".format(chars2[i],chars2[y]))
            y+=1
        print("Combining Chars: {}%".format(str(i/len(chars2)*100)))
        i+=1

    i=0
    getList = list(dictionaryChar)
    while(i<len(dictionaryChar)):
        dictionaryChar.update({getList[i]:chr(i+97)})
        print("Progress {}%".format(str(i/len(dictionaryChar)*100)))
        i+=1

    #print(dictionaryChar.get("aa"))

#print(dictionaryChar)
#sys.exit()

def TranslateT2R(text):
    global dictionaryChar, chars2
    outText=""
    translated=""
    i=0
    while(i<len(text)):
        if text[i] in chars2:
            outText+=text[i]
        i+=1

    if len(outText) % 2 != 0:
        outText = outText[:-1]
        
    i=0
    while(i<len(outText)):
        try:
            #print(outText[i]+outText[i+1])
            translated+= dictionaryChar.get(outText[i]+outText[i+1])
        except Exception as e:
            print(e)
        i+=2
    #print(translated)
    return translated

def TranslateR2T(rare):
    global dictionaryChar, chars2
    outText=""
    keyList = list(dictionaryChar.keys())
    valueList = list(dictionaryChar.values())
    i=0
    while(i<len(rare)):
        outText+=list(keyList)[valueList.index(rare[i])]
        i+=1

    #print(outText)
    return outText

__init__()
print("Initted")
final = TranslateT2R("Hello world")
print(str(final))
TranslateR2T(str(final))

'''

i=97
amountChars = 8010+i
while(i<amountChars):
    chars.append(chr(i))
    #dictionaryChar = dict()
    print("{0:.0%}".format(float(i/amountChars)))
    i+=1


try:
    #print(len(list(combinations(chars,2))))
    pass
except Exception as e:
    print(e)

enc = open("enc",'w')
i=0
while(i<len(chars)):
    try:
        enc.write(str(chars[i].encode(sys.stdout.encoding, errors='replace')) + "\n")
    except Exception as e:
        print(e)
    i+=1
enc.close()

input()
'''
