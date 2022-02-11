"""Usage:
    ark_minter [<ark>]
"""

import random, re, sys
from docopt import docopt


class ARKMinter(): 
    def __init__(self):
        self.extended_digits = '0123456789bcdfghjkmnpqrstvwxz'
        self.ark_re = 'ark:[/]?([0-9]{5})/([0123456789bcdfghjkmnpqrstvwxz]+)'

    def generate_check_digit(self, identifier_without_check_digit):
        """Multiply each characters ordinal value by its position, starting at
           position 1. Sum the products. Then do modulo 29 to get the check digit
           in extended characters. Be sure to start from the first character of 
           the NAAN (e.g. "61001") and be sure to count the '/' between the NAAN
           and NOID as a zero."""

        m = re.search(self.ark_re, identifier_without_check_digit)
        short_identifier = '{}/{}'.format(m.group(1), m.group(2))

        tot = 0
        pos = 1
        for c in short_identifier:
            if self.extended_digits.find(c) > -1:
                tot += (self.extended_digits.find(c) * pos)
            pos += 1
        return self.extended_digits[tot % len(self.extended_digits)]

    def test_ark_regex(self, identifier):
        return re.search(self.ark_re, identifier) != None

    def test_naan(self, identifier):
        return re.search(self.ark_re, identifier).group(1) == '61001'

    def test_check_digit(self, identifier):
        return self.generate_check_digit(identifier[:-1]) == identifier[-1:]

    def validate(self, identifier):
        return all(
            (
                self.test_ark_regex(identifier),
                self.test_naan(identifier),
                self.test_check_digit(identifier),
            )
        )

    def create(self):
        """create a UChicago ARK in the form 'ark:61001/b2.reedeedeedk', where: 
         
           e is an extended digit, 
           d is a digit, 
           and k is a check digit.
    
           Note that all UChicago Library NOIDs use the shoulder "b2", so
           that's hardcoded into this function."""
    
        ark = [
            'ark:61001/b2',
            random.choice(self.extended_digits),
            random.choice(self.extended_digits),
            random.choice(self.extended_digits[:10]),
            random.choice(self.extended_digits),
            random.choice(self.extended_digits),
            random.choice(self.extended_digits[:10]),
            random.choice(self.extended_digits),
            random.choice(self.extended_digits),
            random.choice(self.extended_digits[:10])
        ]
        ark.append(self.generate_check_digit(''.join(ark)))
        return ''.join(ark)


if __name__ == '__main__':
    args = docopt(__doc__)

    minter = ARKMinter()

    if args['<ark>']: 
        print('{} {}'.format(
            args['<ark>'],
            minter.validate(args['<ark>'])
        ))
    else:
        print(minter.create())
