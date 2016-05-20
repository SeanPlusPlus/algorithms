#!/usr/bin/env python


def merge(a, b):
    s = []
    i = 0
    j = 0
    for k in xrange(len(a) + len(b)):
        try:
            a[i]
        except IndexError:  # reached end of a
            return s + b[j:]

        try:
            b[j]
        except IndexError:  # reached end of b
            return s + a[i:]

        if a[i] < b[j]:
            s.append(a[i])
            i += 1
        else:
            s.append(b[j])
            j += 1
    return s


def main():

    a = [3,4,5,6,19,22,29,31]
    b = [1,2,8,9,17,24,27]

    li = merge(a, b)
    print li


if __name__ == '__main__':
    main()
