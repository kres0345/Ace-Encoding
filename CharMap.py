#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from itertools import combinations

#chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '%', '&', '/', '\\', '<', '>', '{', '}', '(', ')', '=', '"', "'", '+', '-', '*', '[', ']', '$', '|', '?', '-', '_', ' ']
chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
#Lowered the supported chars while testing to decrease dictionary building time.

chars = []
dictionaryChar = {}


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

sys.exit()

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
