import re

ZA_FOLA = re.compile('([\u0985-\u09df])\u09cd\u09af')
BA_FOLA = re.compile('([\u0985-\u09ab\u09ad-\u09df])\u09cd\u09ac')

class ShobdoHash:
    TRANSLATION_TABLE = {
        '\u0985': 'a',
        '\u0986': 'a',
        '\u09df': 'a',
        '\u09be': 'a',

        '\u0987': 'i',
        '\u0988': 'i',
        '\u09bf': 'i',
        '\u09c0': 'i',

        '\u0989': 'u',
        '\u098a': 'u',
        '\u09c1': 'u',
        '\u09c2': 'u',

        '\u098f': 'y',
        '\u0990': 'y',
        '\u09c7': 'y',
        '\u09c8': 'y',

        '\u0993': 'o',
        '\u0994': 'o',
        '\u09cb': 'o',
        '\u09cc': 'o',

        '\u0995': 'k',
        '\u0996': 'k',

        '\u0997': 'g',
        '\u0998': 'g',

        '\u099a': 'c',
        '\u099b': 'c',

        '\u099c': 'j',
        '\u099d': 'j',
        '\u09af': 'j',

        '\u099f': 't',
        '\u09a0': 't',

        '\u09a1': 'd',
        '\u09a2': 'd',

        '\u09a8': 'n',
        '\u09a3': 'n',

        '\u09a4': 'f',
        '\u09a5': 'f',

        '\u09a6': 'q',
        '\u09a7': 'q',

        '\u09aa': 'p',
        '\u09ab': 'p',

        '\u09ac': 'b',
        '\u09ad': 'b',

        '\u09ae': 'm',
        '\u0982': 'm',
        '\u0999': 'm',

        '\u09b0': 'r',
        '\u09dc': 'r',
        '\u09dd': 'r',

        '\u09b6': 's',
        '\u09b7': 's',
        '\u09b8': 's',

        '\u09b9': 'h',
        '\u0983': 'h',

        '\u09b2': 'l',
    }

    def __init__(self):
        self.TRANSLATION_TABLE = {ord(k): ord(v) for k, v in self.TRANSLATION_TABLE.items()}

    def __call__(self, s: str):
        return self.preprocess(s).translate(self.TRANSLATION_TABLE).replace('\u09cd', '')

    def preprocess(self, s: str):
        s = ZA_FOLA.sub('\\1\\1', s)
        s = BA_FOLA.sub('\\1', s)
        return s
