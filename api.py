import random, re
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ARKManager(): 
    def __init__(self):
        self.extended_digits = '0123456789bcdfghjkmnpqrstvwxz'

    def generate_check_digit(self, identifier):
        """Multiply each characters ordinal value by its position, starting at
           position 1. Sum the products. Then do modulo 29 to get the check digit
           in extended characters."""

        m = re.search('ark:[/]?([0-9]{5}/[0-9a-z]+)', identifier)
        short_identifier = m.group(1)

        i = 0
        pos = 1
        for c in short_identifier:
            if self.extended_digits.find(c) > -1:
                i += (self.extended_digits.find(c) * pos)
            pos += 1
        return self.extended_digits[i % len(self.extended_digits)]

    def test_noid_check_digit(self, identifier):
        return self.generate_check_digit(identifier[:-1]) == identifier[-1:]

    def create(self):
        """create a UChicago ARK in the form 'ark:61001/b2.reedeedeedk', where: 
         
           e is an extended digit, 
           d is a digit, 
           and k is a check digit.
    
           Note that all UChicago Library NOIDs start with the prefix "b2", so
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


class ARKValidator(Resource):
    def get(self):
        id = request.args['id']

        # ARKs
        m = re.search('^ark:/?([0-9]{5})/([a-z0-9]+)$', id)
        if m:
            naan = m.group(0)
            assigned_name = m.group(1)
            am = ARKManager()
            print(id)
            if am.test_noid_check_digit(id) == False:
                return {id: 'invalid'}
        else:
            raise NotImplementedError
        return {id: 'valid'}

api.add_resource(ARKValidator, '/validate')

class ARKGenerator(Resource):
    def get(self):
        am = ARKManager()
        return {am.create(): 'valid'}

api.add_resource(ARKGenerator, '/generate')

if __name__ == '__main__':
    app.run(debug=True)
