#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import textprocessor

tokenizer = re.compile(r'(\d+)').split


def convert(token):
    if token != '0' and token.startswith('0'):
        return token
    return str(int(token) + 1)


def increment(line):
    tokens = tokenizer(line)
    tokens = [x if i % 2 == 0 else convert(x) for (i, x) in enumerate(tokens)]
    print(''.join(tokens))


if __name__ == '__main__':
    textprocessor.process(increment)
