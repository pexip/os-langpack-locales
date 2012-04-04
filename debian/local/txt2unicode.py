#!/usr/bin/python
# Convert a line from stdin to the U<XXXX> notation used in locales
# Author: Martin Pitt <martin.pitt@ubuntu.com>
# License: Public Domain

import sys

line = sys.stdin.readline().decode('UTF-8')
for c in line.strip():
    sys.stdout.write('<U%04X>' % ord(c))
print
