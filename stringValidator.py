if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    if(s.isalpha()):
        print(False)
    else:
        print(True)
        
    if(s.isdigit()):
        print(False)
    else:
        print(True)
    if(s.isupper()):
        print(False)
    else:
        print(True)
        
    if(s.islower()):
        print(False)
    else:
        print(True)
