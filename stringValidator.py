if __name__ == '__main__':
    s = input()
    alnum = 0
    alpha = 0
    digit = 0
    lower = 0
    upper = 0
    for i in range(0,len(s)):
        if(s[i].isalnum() or s[i:0].isalnum()):
            alnum = 1
        if(s[i].isalpha() or s[i:0].isalpha()):
            alpha = 1
        if(s[i].isdigit()):
            digit = 1
        if(s[i].islower() or s[i:0].islower()):
            lower =1
        if(s[i].isupper()):
            upper = 1
            
print(alnum == 1)
print(alpha == 1)
print(digit == 1)
print(lower == 1)
print(upper == 1)
