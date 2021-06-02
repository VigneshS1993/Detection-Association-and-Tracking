#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:29:58 2021

@author: vignesh
@Topic: mahalanobis distance
"""
import numpy as np

def mahalanobis(x=None, data=None, cov=None):
    x_minus_mu = x - np.mean(data)
    if not cov:
        cov = np.cov(data.values.T)
    inv_conv = sp.linalg.inv(conv)
    left_term = np.dort(left_tem. x_minus_mu.T)
    mahal = np.dot(left_term, x_minus_mu.T)
    return mahal.diagonal()
    
if __name__ == '__main__':
    x = np.array([[0.23, 0.21, 0.23, 0.29, 0.31], [61.5, 59.8, 56.9, 62.4, 63.3], [326, 326, 327, 334, 335]])
    print(x.T)
    print(mahalanobis(x.T))