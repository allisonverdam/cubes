# -*- encoding: utf-8 -*-
"""Pytho compatibility utilities"""



import sys

py3k = sys.version_info >= (3, 0)

if py3k:
    string_type = str
    binary_type = bytes
    text_type = str
    int_types = int,
    iterbytes = iter

    from urllib.parse import urlparse
    from urllib.request import urlopen, build_opener
    from urllib.request import HTTPPasswordMgrWithDefaultRealm
    from urllib.request import HTTPBasicAuthHandler
    from urllib.parse import urlencode
    from configparser import ConfigParser
    from io import StringIO
    from queue import Queue
    from functools import reduce

    def to_unicode(s):
        return str(s)

    def to_str(b):
        return b.decode("utf-8")

    def open_unicode(filename):
        return open(filename, encoding="utf-8")

else:
    string_type = str
    binary_type = str
    text_type = str
    int_types = int, int

    from urllib.parse import urlparse
    from urllib.request import urlopen, build_opener
    from urllib.request import HTTPPasswordMgrWithDefaultRealm
    from urllib.request import HTTPBasicAuthHandler
    from urllib.parse import urlencode
    from configparser import SafeConfigParser as ConfigParser
    from io import StringIO
    from queue import Queue
    reduce = reduce

    def to_str(b):
        return b

    def to_unicode(s):
        if isinstance(s, str):
            return s
        s = str(s)
        for enc in ('utf8', 'latin-1'):
            try:
                return str(s, enc)
            except UnicodeDecodeError:
                pass

        raise ValueError("Cannot decode for unicode using any of the default "
                         "encodings: %s" % s)

    def open_unicode(filename):
        return open(filename)
