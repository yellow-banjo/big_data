#!/usr/bin/env python

import sys

cnt, mean, var = 0, 0, 0

for line in sys.stdin:
    ck, mk, vk = line.strip().split('\t')
    ck = int(ck)
    mk, vk = float(mk), float(vk)
    var = (cnt * var + ck * vk) / (cnt + ck) + cnt * ck * ((mean - mk) / (cnt + ck)) ** 2
    mean = (cnt * mean + ck * mk) / (cnt + ck)
    cnt += ck
    
print("{}\t{}".format(mean, var))