"""
Ask for an input binary file to calculate an MD5 checksum.
Ask for a file ending in .md5 with the correct checksum.
Output the results and compare.

Future:
    - implement a way to compare a list of files

Note: MD5 is deprecated. SHA-1 is preferred
"""
import hashlib
import os
import sys

blocksize = 65535

print('Compare the MD5 hash of a binary file and its hash file.')
print('\nEnter the name of the binary file to calculate the hash:')
fin = input('>> ')
if not os.path.exists(fin):
    print('Error - file not found:', fin)
    print('Exiting')
    sys.exit(1)
print("Enter the file containing the distributor's MD5 hash:")

hashfile = input('>> ')
if not os.path.exists(hashfile):
    print('Error - file not found:', hashfile)
    print('Exiting')
    sys.exit(1)
hashstr = open(hashfile).readline().strip()

# Initialize the MD5 hasher
hasher = hashlib.md5()

# Read the file and calculate the hash
print('Calculating md5 hash of', fin)
with open(fin, 'rb') as f:
    blocks_read = 0
    while True:
        data = f.read(blocksize)
        if not data:
            break
        blocks_read += len(data)
        hasher.update(data)
    print('Read {} bytes'.format(blocks_read))

# Output the results
print('-'*30, 'Results', '-'*30)
print(' Calculated MD5 hash: {}'.format(hasher.hexdigest()))
print('Distributed MD5 hash: {}'.format(hashstr))
print('-'*69)
match = False
if hasher.hexdigest() == hashstr:
    match = True

if match:
    print(' '*10, 'The Results Match')
else:
    print(' '*5, '*'*5, 'The Results DO NOT MATCH', '*'*5, ' '*5)
print('-'*69, '\n\n')
