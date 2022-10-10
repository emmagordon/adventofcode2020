#!/usr/bin/env python3

import re

PUZZLE_INPUT = "input.txt"

class Passport:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_fields = ['cid']

    def __init__(self, passport_str):
        details = {
            k: v for k, v in [
                field.split(':') for field in passport_str.lstrip().split()
            ]
        }
        self.details = details
    
    @property
    def is_valid(self):
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

        if not all(k in self.details for k in Passport.required_fields):
            return False
        if not _validate_num(self.details['byr'], 1920, 2002):
            return False
        if not _validate_num(self.details['iyr'], 2010, 2020):
            return False
        if not _validate_num(self.details['eyr'], 2020, 2030):
            return False
        if not self.details['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if not re.match('#[0-9a-f]{6}', self.details['hcl']):
            return False
        if not re.match('[0-9]{9}', self.details['pid']):
            return False
        
        hgt = self.details['hgt']
        if hgt.endswith('cm'):
            if not _validate_num(hgt[:-2], 150, 193):
                return False
        elif hgt.endswith('in'):
            if not _validate_num(hgt[:-2], 59, 76):
                return False
        else:
            return False
        
        return True

    def __repr__(self):
        return f"{self.details}"


def _validate_num(num_str, _min, _max):
    try:
        byr = int(num_str)
    except ValueError:
        return False
    else:
        return _min <= byr <= _max


def parse(puzzle_input):
    entries = []
    entry = ""
    for line in puzzle_input:
        if line:
            entry += f" {line}"
        else:
            entries.append(Passport(entry))
            entry = ""
    
    if entry:
        entries.append(Passport(entry))
    
    return entries

if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    valid_passports = [
        passport for passport in parse(puzzle_input) if passport.is_valid
    ]
    
    for p in valid_passports[:5]:
        print(p)
        print('\n')

    print(len(valid_passports)) # 189, but should be 188
