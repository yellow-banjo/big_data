#!/usr/bin/env python

import sys
from csv import reader

ck, mk, vk = 0, 0, 0

for line in reader(sys.stdin):
    try:
        cur = float(line[9])
        vk = ck * vk / (ck + 1) + ck * ((mk - cur) / (ck + 1)) ** 2
        mk = (ck * mk + cur) / (ck + 1)
        ck += 1
    except:
        continue
        
print("{}\t{}\t{}".format(ck, mk, vk))