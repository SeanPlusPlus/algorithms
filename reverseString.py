def reverseString(s):
    if s == "":
        return s
    else:
        return s[1:] + s[0]

def main():
    mystr = 'hello'
    r = reverseString(mystr)
    print mystr, r

if __name__ == '__main__':
    main()

