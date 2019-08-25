def combineStringArray(wordArray):
    word = ""
    for char in wordArray:
        word += char

    return(word)

def genStringArray(word):
    stringArray = [] 
    for char in word:
        stringArray.append(char)

    return(stringArray)


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    shiftAmount = n
    stringArray = genStringArray(string) 
    rotatedString = ""
     
    if shiftAmount < 0:
        for i in range(abs(n)):
            char = stringArray.pop()
            stringArray.insert(0, char)
        return(combineStringArray(stringArray))
      
    if shiftAmount > 0:
        for i in range(abs(n)):
            char = stringArray.pop(0)
            stringArray.append(char)
        return(combineStringArray(stringArray))

    if shiftAmount == 0:
        return(combineStringArray(stringArray))


