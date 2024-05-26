def mutate_string(string, position, character):
    strg=list(string)
    pos=position
    char=character
    strg[pos]=char
    altStr=''.join(strg)
    return altStr

if __name__ == '__main__':
