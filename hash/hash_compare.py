#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: hash_compare.py

This script is written for Python 3.4 with no gaurantees of
    backwards compatibility.

This script calculates MD5 or SHA hashes on a series of objects and
compares them to the values provided.

Supported hash algorithms are derived from hashlib.algorithms_available

Input:
     hashfile: the file listing the objects to compare and their hashes
         format of hashfile:
             field 1: object name
             field 2: hash algorithm
             field 3: distributor provided hash
             fields are separated by a ':'

             ex: object_bin-1.2.tar.gz:sha1:1245l26k2451234
"""
import hashlib
import os
import sys

"""
Data list to store values.
A single entry is a dict of the following values:
    - 'object': the object name to compare
    - 'alg': the algorithm used for the hash
    - 'prov_hash': the hash value provided by the vendor
    - 'calc_hash': the hash value calculated by this script
    - 'match': a boolean True/False comparison of the two hashes
"""
def load_file(hashfile):
    """
    Load the file containing processing information
    and check for proper formatting.
    """
    with open(hashfile) as fin:
        for entry in fin.readlines():
            data.append(check_format(entry))

def check_format(entry):
    """
    Provided a single-line entry, check the format.
    Ensure it has three items. The first item should be a file that
    exists, and the second item should be a supported hash.

    Return a dict with keys 'file', 'alg', 'prov_hash'.
    Raise a BadFormatException if entry is bad.
    """
    values = ':'.split(entry).strip()
    # Check if values[0] exists
    if not os.path.exists(values[0]):
        raise BadFormatException('File {} does not exist'.format(values[0]))
    # Check if values[1] is a supported algorithm
    if not values[1] in hashlib.algortihms_available:
        raise BadFormatException('Algorithm {} is not supported'.format(values[1]))
    # Check to see if a hash was provided
    #TODO: implement a format checking for provided hashes
    if not values[2]:
        raise BadFormatException('No distributor has provided')
    res = {
            'file': values[0],
            'alg': values[1],
            'prov_hash': values[2],
            'calc_hash': '',
            'match': False
           }
    # 'calc_hash' and 'match' will be computed later
    return res

def calc_hashes():
    """Calculate the hashes of the objects."""
    pass

def compare_hashes():
    """Compare calculated hashes to supplied hashes."""
    pass
def report():
    """Report results to screen and to an output file 'results.txt'."""
    pass

class BadFormatException(Exception):
    """Error thrown when hashfile doesn't meet correct format."""
    def __init__(self, entry):
        self.entry = entry

    def __str__(self):
        return """
               An improperly formatted entry was detected.
               Please make sure to use the following format:
                   <object name> : <hash algorithm > : <provided hash>
               Supported hashes are:
                """ + hashlib.algorithms_available +
                "The erroneous entry is: " + entry


if __name__ == '__main__':
    hashfile = 'hashes.txt'          # The default file if none provided
    if sys.argv[1]:             # Filename provided, sanity check
        if not os.path.exists(sys.argv[1]):
            print('Error: file {} does not exists'.format(sys.argv[1]))
        else:
            hashfile = sys.argv[1]
    load_file(hashfile)
