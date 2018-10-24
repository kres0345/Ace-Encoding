# Ace-Encoding
An encoding language that has an expansion rate of 2:1.

### Calculations
Chars available: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 ! @ # % & / \ < > { } ( ) = " ' + - * [ ] $ | ? - _ ` that's 89 characters(incl. space). That's a lot.

To make the ratio 2:1 I'll have 1 char represent 1 or 2 characters at once. What that means is that I'll use:
`(89 * 89) + 89`, individual characters. EDIT: I'll need new calculations as these are outdated.

### Practice
 - CharMapModule.py.

```python
NAME
    CharMapModule - # -*- coding: utf-8 -*-

FUNCTIONS
    BuildDictionary(logging=False)

    SetCharset(List)
        :param List: A list of the new charset.
        :return: True if ran correct, false if not.

    TranslateR2T(rare)
        :param rare: The rare text created using the exact same charset.
        :return: Translated text.

    TranslateT2R(text)
        :param text: The input string.
        :return: The text translated into rare.

    __init__()

DATA
    chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', ...
    dictionaryChar = {}
```
 - AceCompressor.py

AceCompressor is a program that compresses files, but I havent finished it — and I am not planning to.

 - CharMap.py

More like a demo, the first file I worked on, the code from this file have been migrated to CharMapModule.py.

### Demo code
```python
import CharMapModule as CMM
CMM.BuildDictionary()
encodedtext = CMM.TranslateT2R("Hello world")
print( "Encoded: " + str(encodedtext) )
print( "Decoded: " + CMM.TranslateR2T(encodedtext) )
```
Note: When decoded it should output "Hello Worl", because the number of letters in "Hello World" is uneven. When the string length is uneven it cuts off the last character
