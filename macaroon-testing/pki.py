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
class AttrCert:
    def __init__(self,v,h,i,s,sno,valid,attr):
        self.version = v
        self.holder = h
        self.issuer = i
        self.sign_algo = s
        self.sno = sno
        self.validity = valid
        self.attr = attr
        self.signature = None
    def print_attr(self):
        return self.version+"\n"+self.holder+"\n"+self.issuer+"\n"+self.sign_algo+"\n"+self.sno+"\n"+self.validity+"\n"+self.attr
        

from Crypto.PublicKey import RSA
avg_gen = 0.0
avg_sign = 0.0
avg_verify = 0.0
keys = [1024,2048,4096]
for j in range(3):

    for i in range(10):
        start = time.time()
        key = RSA.generate(keys[j])
        avg_gen = avg_gen+time.time()-start
        attr = AttrCert("1.0","meter","utility","RSA","1","Feb 2017","Belongs to this user")
        start = time.time()
        sign =  key.sign(attr.print_attr(),None)
        avg_sign = avg_sign+time.time()-start
        start = time.time()
        x =  key.verify(attr.print_attr(),sign)
        avg_verify = avg_verify+time.time()-start
    print "Minting attr cert",(avg_gen+avg_sign)/10
    print "Verification:",avg_verify/10
