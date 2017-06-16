import string
import hashlib

def sha1_hexdigest(value):
    return hashlib.sha1(value).hexdigest()

def sha256_hexdigest(value):
    return hashlib.sha256(value).hexdigest()

def escape_file_name(value):
    return value.replace(u'/', u'\u2215')

from slugify import slugify

class Formatter(string.Formatter):

    def __init__(self):
        self.conversions = {
                'x': sha1_hexdigest,
                'X': sha256_hexdigest,
                'f': escape_file_name,
                'g': slugify
                }
        pass

    def convert_field(self, value, conversion):
        if conversion in self.conversions:
            return self.conversions[conversion](value)
        return super(Formatter, self).convert_field(value, conversion)

