#!/usr/bin/env python
# -*- coding: utf-8 -*-

import textprocessor


def identity(line):
    print(line)


if __name__ == '__main__':
    textprocessor.process(identity)
