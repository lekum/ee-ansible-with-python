def rot13(s):
    def lookup(v):
        o, c = ord(v), v.lower()
        if 'a' <= c <= 'm':
            return chr(o + 13)
        if 'n' <= c <= 'z':
            return chr(o - 13)
        return v
    return ''.join(map(lookup, s))

class FilterModule(object):

    def filters(self):
        return {
                'rot13': rot13
               }
