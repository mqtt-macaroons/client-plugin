#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 prashant <prashant@prashant-Geekpad>
#
# Distributed under terms of the MIT license.

"""

"""

import time
from Crypto.Cipher import AES
from macaroon import Macaroon
from macaroon import Caveat
import random

avg_mint = 0.0
avg_verify = 0.0
for i in range(10):
    start_time = time.time()

    r = random.SystemRandom()
    key = r.getrandbits(32)
    m = Macaroon(1,key)
    cav = Caveat("Issuer = Utility")
    m.add_cav(cav)
    cav = Caveat("Recipient = Smart Meter")
    m.add_cav(cav)
    cav = Caveat("Valid till : Feb 1 2017")
    m.add_cav(cav)
    end_time = time.time()
    avg_mint = avg_mint+ end_time-start_time

    start_time = time.time()
    m.verify(key)
    avg_verify= avg_verify+ time.time()-start_time

print "Mint : ", avg_mint/10
print "Verify :",avg_verify/10

