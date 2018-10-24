#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from itertools import combinations
global dictionaryChar, chars2
dictionaryChar = {}
chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']


def __init__():
    global dictionaryChar, chars2


def TranslateT2R(text):
    """
    :param text: The input string.
    :return: The text translated into rare.
    """
    #global dictionaryChar, chars2
    rare = ""
    translated = ""

    for i in range(len(text)):
        if text[i] in chars2:
            rare += text[i]

    if len(rare) % 2 != 0:
        rare = rare[:-1]

    i = 0
    while i < len(rare):
        try:
            translated += dictionaryChar.get(rare[i] + rare[i+1])
        except Exception as e:
            print(e)
        i += 2
    return translated


def TranslateR2T(rare):
    """
    :param rare: The rare text created using the exact same charset.
    :return: Translated text.
    """
    #global dictionaryChar, chars2
    text = ""
    keys = list(dictionaryChar.keys())
    values = list(dictionaryChar.values())

    for i in range(len(rare)):
        text += list(keys)[values.index(rare[i])]

    return text


def SetCharset(List):
    """
    :param List: A list of the new charset.
    :return: True if ran correct, false if not.
    """
    global chars2
    if isinstance(List, (list,)):
        chars2 = List
        return True
    return False


def BuildDictionary(logging=False):
    global dictionaryChar
    dictionaryChar = {}
    for i in range(len(chars2)):
        for y in range(len(chars2)):
            dictionaryChar.update({"{}{}".format(chars2[i],chars2[y]):0})
        if logging:
            print("Combining characters: {}%".format(str(i/len(chars2)*100)))

    getList = list(dictionaryChar)
    for i in range(len(dictionaryChar)):
        dictionaryChar.update({getList[i]:chr(i+97)})
        if logging:
            print("Building {}%".format(str(i/len(dictionaryChar)*100)))


__init__()