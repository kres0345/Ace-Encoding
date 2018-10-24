# Ace-Encoding
An encoding language that has an expansion rate of 2:1.

### Calculations
Chars available: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 ! @ # % & / \ < > { } ( ) = " ' + - * [ ] $ | ? - _ ` that's 89 characters(incl. space). That's a lot.

To make the ratio 2:1 I'll have 1 char represent 1 or 2 characters at once. What that means is that I'll use:
`(89 * 89) + 89`, individual characters. EDIT: I'll need new calculations as these are outdated.

### Practice
- CharMapModule.py
`CharMapModule.TranslateT2R(string)`
Returns the now-encoded-string, using the charset specified at top of CharMapModule.py.
`CharMapModule.TranslateR2T(rare)`
Returns the now-decoded-rare, translated back using the charset specified at top of CharMapModule.py.
`CharMapModule.__init__()`
Creates the dictionary based on the charset.
