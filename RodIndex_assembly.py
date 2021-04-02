#!/usr/bin/env python
#! -*- coding:utf-8 -*-

# SmAHTR rod in assembly index.
with open('cell_index.txt', 'w') as f:
    for i in range(-5, 6):
        if i < 0:
            for j in range(-5-i, 6):
                f.write('84005[%d %d 0]<84013[0 0 0]\n' % (i, j))
        elif i > 0:
            for j in range(-5, 6-i):
                f.write('84005[%d %d 0]<84013[0 0 0]\n' % (i, j))
        elif i == 0:
            for j in range(-5, 6):
                f.write('84005[%d %d 0]<84013[0 0 0]\n' % (i, j))

print('done...')
# the result:
# [-5 0 0]
# [-5 1 0]
# [-5 2 0]
# [-5 3 0]
# [-5 4 0]
# [-5 5 0]
# c ccccccccccccccccccc c
# [-4 -1 0]
# [-4 0 0]
# [-4 1 0]
# [-4 2 0]
# [-4 3 0]
# [-4 4 0]
# [-4 5 0]
# c ccccccccccccccccccc c
# [-3 -2 0]
# [-3 -1 0]
# [-3 0 0]
# [-3 1 0]
# [-3 2 0]
# [-3 3 0]
# [-3 4 0]
# [-3 5 0]
# c ccccccccccccccccccc c
# [-2 -3 0]
# [-2 -2 0]
# [-2 -1 0]
# [-2 0 0]
# [-2 1 0]
# [-2 2 0]
# [-2 3 0]
# [-2 4 0]
# [-2 5 0]
# c ccccccccccccccccccc c
# [-1 -4 0]
# [-1 -3 0]
# [-1 -2 0]
# [-1 -1 0]
# [-1 0 0]
# [-1 1 0]
# [-1 2 0]
# [-1 3 0]
# [-1 4 0]
# [-1 5 0]
# c ccccccccccccccccccc c
# [0 -5 0]
# [0 -4 0]
# [0 -3 0]
# [0 -2 0]
# [0 -1 0]
# [0 0 0]
# [0 1 0]
# [0 2 0]
# [0 3 0]
# [0 4 0]
# [0 5 0]
# c ccccccccccccccccccc c
# [1 -5 0]
# [1 -4 0]
# [1 -3 0]
# [1 -2 0]
# [1 -1 0]
# [1 0 0]
# [1 1 0]
# [1 2 0]
# [1 3 0]
# [1 4 0]
# c ccccccccccccccccccc c
# [2 -5 0]
# [2 -4 0]
# [2 -3 0]
# [2 -2 0]
# [2 -1 0]
# [2 0 0]
# [2 1 0]
# [2 2 0]
# [2 3 0]
# c ccccccccccccccccccc c
# [3 -5 0]
# [3 -4 0]
# [3 -3 0]
# [3 -2 0]
# [3 -1 0]
# [3 0 0]
# [3 1 0]
# [3 2 0]
# c ccccccccccccccccccc c
# [4 -5 0]
# [4 -4 0]
# [4 -3 0]
# [4 -2 0]
# [4 -1 0]
# [4 0 0]
# [4 1 0]
# c ccccccccccccccccccc c
# [5 -5 0]
# [5 -4 0]
# [5 -3 0]
# [5 -2 0]
# [5 -1 0]
# [5 0 0]
# c ccccccccccccccccccc c
