from operator import itemgetter

def create_hoffman_dict(text):
    """
    Input text is a string containing the text you want to encode.
    """
    chars = []
    combochars = []

    for i in range(len(text)):
        if not text[i] in chars:
            chars.append(text[i])
            

    for i in range(len(chars)):
        for y in range(len(chars)):
            charcombo = chars[i] + chars[y]
            charcount = text.count(charcombo)
            combochars.append({"char": charcombo, "count": charcount})

    combochars = sorted(combochars, key=itemgetter('count'),reverse=True)

    combochars_new = []
    
    for i in range(len(combochars)):
        combochars_new.append(combochars[i]['char'])
    combochars = combochars_new

    dictionary = {}

    for i in range(len(combochars)):
        dictionary[combochars[i]] = chr(i)#+97 # Previusly I started building from 97
                                        #But then I'ld just skip 97 1 byte chars.

    return dictionary


#print(create_hoffman_dict(open('Encode this.txt').read()))
