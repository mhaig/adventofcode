#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import hashlib
import sys

def mine(secret_key, zeros):

    print("mining for {} zeros with secret key '{}'".format(zeros, secret_key))

    number = 1
    m = hashlib.md5()
    m.update('{}{}'.format(secret_key, number).encode('utf-8'))
    while m.hexdigest()[0:5] != '0'*zeros:
        number += 1
        m = hashlib.md5()
        m.update('{}{}'.format(secret_key, number).encode('utf-8'))


    return number

if __name__ == '__main__':
    secret_key = sys.stdin.read()
    print(mine(secret_key.strip(), 5))
    print(mine(secret_key.strip(), 6))
