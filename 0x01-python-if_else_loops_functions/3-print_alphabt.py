#!/usr/bin/python3
skip = {'e', 'q'}
skipped = ''
for Ascii in range(97, 123):
    if chr(Ascii) not in skip:
        skipped += chr(Ascii)
print(skipped, end='')
