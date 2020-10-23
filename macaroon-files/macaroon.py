#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 prashant <prashant@prashant-Geekpad>
#
# Distributed under terms of the MIT license.

"""

"""
from Crypto.Hash  import MD5,SHA,SHA256
import random 
algo = SHA #MD5, SHA, SHA256
class Caveat:
    def __init__(self,r):
        self.rule = r
        self.cav = None
    def add_rule(self,rule):
        self.rule = rule
class Macaroon:
    def __init__(self,m_id,key):
        self.m_id = m_id
        r = random.SystemRandom()
        nonce = r.getrandbits(10)
        cave= Caveat(str(nonce))
        self.caveats=None
        self.hmac = None
        self.add_cav(cave,key)
    def add_cav(self,cav,key=0):
        cave = self.caveats
        if(cave!=None):
            while(cave.cav!=None):
                cave = cave.cav
            cave.cav = cav
        else:
            self.caveats=cav
        if(self.hmac!=None):
            temp_h = algo.new(self.hmac.hexdigest())
        else:
            temp_h = algo.new(str(key))
        temp_h.update(cav.rule)
        self.hmac = temp_h
    def printing(self):
        cav = self.caveats
        while(cav!=None):
            print cav.rule
            cav = cav.cav
        print self.hmac.hexdigest()

    def verify(self,key):
        cave = self.caveats
        h = algo.new(str(key))
        temp = h
        while(cave!=None):
            h.update(cave.rule)
            cave = cave.cav
            temp = h
            h = algo.new(temp.hexdigest())
        print temp.hexdigest() == self.hmac.hexdigest()


