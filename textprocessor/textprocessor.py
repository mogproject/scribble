#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helper function for text stream processing
"""

import sys


def process(function):
    paths = (sys.argv + [None])[1:max(2, len(sys.argv))]
    for path in paths:
        try:
            fp = sys.stdin if path is None else open(path)
            for line in fp:
                function(line.rstrip("\n"))
        except (KeyboardInterrupt, EOFError):
            pass
        except Exception:
            exc_type, exc = sys.exc_info()[:2]
            print('%s: %s: %s' % (sys.argv[0], exc_type.__name__, exc))
