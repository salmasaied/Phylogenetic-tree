# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:32:49 2020

@author: Salma Muhammad Saied
"""

import  numpy as np
import math

def distance(seq1,seq2):
    x=0
    d=abs(len(seq1)-len(seq2))
    if len(seq1)>len(seq2):
        seq2+=d*'-'
    else:
        seq1+=d*'-'
    for i in range(len(seq2)):
        if (seq1[i]!=seq2[i]):
            x+=1
    return x

def mincell(table):
    min_cell = float("inf")
    x, y =-1,-1

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_cell:
                min_cell = table[i][j]
                x, y = i, j

    return x, y

def SETUPGMA(sequences):
    matrix=np.zeros((len(sequences),len(sequences)))
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            matrix[i][j] = math.inf
    for i in range (len(sequences)):
        for j in range(i):
            matrix[i][j]=distance(sequences[i],sequences[j])
    print(matrix)
    while(len(matrix[0])>=2):
        minx,miny=mincell(matrix)
        if((minx==-1)&(miny==-1)):
            break
        print('merge cluster',miny,"int ",minx)
        print(matrix)
        for i in range(len(matrix[0])):
            matrix[miny][i]=(matrix[miny][i]+matrix[minx][i])/2
        matrix=np.delete(matrix,minx,0)
        matrix=np.delete(matrix,minx,1)


SETUPGMA(['AAAG','AAAC','ATGC','CCGG','GTAG','AACT'])
seq1='ATT'
seq2='AT'
print(distance(seq1,seq2))
print(mincell([[22,0,1,2,3],[4,5,7,8]]))