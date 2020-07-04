#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np

class Functions():
    def __init__(self):
        self.aprox_a = 0.0227
        self.aprox_b = -0.3794
        self.aprox_c = 4.6459

    def convBulr(self, vec, rate=None, frame=None):
        if not rate is None:
            rate = rate // 1000
            frame = int(self.aprox_a*math.pow(rate, 2) + self.aprox_b*rate + self.aprox_c)
            print(frame)

        if frame is None: return vec

        #frame = frame // 3

        if not frame % 2: frame -= 1

        hf = frame // 2
        blur = [ 0 for el in range(hf)] #add first elements not used in loop below 
        for step in range(hf, len(vec) - hf):
            blur.append( int( np.mean(vec[step - hf : step + hf])))
        blur += [0 for el in range(hf)] #add last elements not used in loop below 
        
        return blur
        

if __name__ == "__main__":
    function = Functions()
    vec = [1, 2, 3, 4, 5, 6, 9, 2, 2, 4, 4 ,6, 7, 4, 188, 4 , 3, 4, 56, 3]
    function.convBulr(vec, rate=8100)
        
