def isPal(li):
    if len(li) <= 1:
        return True
    back = li.pop()
    front = li.pop(0)
    if back != front:
        return False
    return isPal(li)

def main():
    s1 = 'racecar'
    print isPal([c for c in s1])

    s2 = 'hello'
    print isPal([c for c in s2])

    s3 = 'a'
    print isPal([c for c in s3])

if __name__ == '__main__':
    main()

