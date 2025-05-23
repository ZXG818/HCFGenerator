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
# 84005[-5 0 0]<84013[0 0 0]
# 84005[-5 1 0]<84013[0 0 0]
# 84005[-5 2 0]<84013[0 0 0]
# 84005[-5 3 0]<84013[0 0 0]
# 84005[-5 4 0]<84013[0 0 0]
# 84005[-5 5 0]<84013[0 0 0]
# 84005[-4 -1 0]<84013[0 0 0]
# 84005[-4 0 0]<84013[0 0 0]
# 84005[-4 1 0]<84013[0 0 0]
# 84005[-4 2 0]<84013[0 0 0]
# 84005[-4 3 0]<84013[0 0 0]
# 84005[-4 4 0]<84013[0 0 0]
# 84005[-4 5 0]<84013[0 0 0]
# 84005[-3 -2 0]<84013[0 0 0]
# 84005[-3 -1 0]<84013[0 0 0]
# 84005[-3 0 0]<84013[0 0 0]
# 84005[-3 1 0]<84013[0 0 0]
# 84005[-3 2 0]<84013[0 0 0]
# 84005[-3 3 0]<84013[0 0 0]
# 84005[-3 4 0]<84013[0 0 0]
# 84005[-3 5 0]<84013[0 0 0]
# 84005[-2 -3 0]<84013[0 0 0]
# 84005[-2 -2 0]<84013[0 0 0]
# 84005[-2 -1 0]<84013[0 0 0]
# 84005[-2 0 0]<84013[0 0 0]
# 84005[-2 1 0]<84013[0 0 0]
# 84005[-2 2 0]<84013[0 0 0]
# 84005[-2 3 0]<84013[0 0 0]
# 84005[-2 4 0]<84013[0 0 0]
# 84005[-2 5 0]<84013[0 0 0]
# 84005[-1 -4 0]<84013[0 0 0]
# 84005[-1 -3 0]<84013[0 0 0]
# 84005[-1 -2 0]<84013[0 0 0]
# 84005[-1 -1 0]<84013[0 0 0]
# 84005[-1 0 0]<84013[0 0 0]
# 84005[-1 1 0]<84013[0 0 0]
# 84005[-1 2 0]<84013[0 0 0]
# 84005[-1 3 0]<84013[0 0 0]
# 84005[-1 4 0]<84013[0 0 0]
# 84005[-1 5 0]<84013[0 0 0]
# 84005[0 -5 0]<84013[0 0 0]
# 84005[0 -4 0]<84013[0 0 0]
# 84005[0 -3 0]<84013[0 0 0]
# 84005[0 -2 0]<84013[0 0 0]
# 84005[0 -1 0]<84013[0 0 0]
# 84005[0 0 0]<84013[0 0 0]
# 84005[0 1 0]<84013[0 0 0]
# 84005[0 2 0]<84013[0 0 0]
# 84005[0 3 0]<84013[0 0 0]
# 84005[0 4 0]<84013[0 0 0]
# 84005[0 5 0]<84013[0 0 0]
# 84005[1 -5 0]<84013[0 0 0]
# 84005[1 -4 0]<84013[0 0 0]
# 84005[1 -3 0]<84013[0 0 0]
# 84005[1 -2 0]<84013[0 0 0]
# 84005[1 -1 0]<84013[0 0 0]
# 84005[1 0 0]<84013[0 0 0]
# 84005[1 1 0]<84013[0 0 0]
# 84005[1 2 0]<84013[0 0 0]
# 84005[1 3 0]<84013[0 0 0]
# 84005[1 4 0]<84013[0 0 0]
# 84005[2 -5 0]<84013[0 0 0]
# 84005[2 -4 0]<84013[0 0 0]
# 84005[2 -3 0]<84013[0 0 0]
# 84005[2 -2 0]<84013[0 0 0]
# 84005[2 -1 0]<84013[0 0 0]
# 84005[2 0 0]<84013[0 0 0]
# 84005[2 1 0]<84013[0 0 0]
# 84005[2 2 0]<84013[0 0 0]
# 84005[2 3 0]<84013[0 0 0]
# 84005[3 -5 0]<84013[0 0 0]
# 84005[3 -4 0]<84013[0 0 0]
# 84005[3 -3 0]<84013[0 0 0]
# 84005[3 -2 0]<84013[0 0 0]
# 84005[3 -1 0]<84013[0 0 0]
# 84005[3 0 0]<84013[0 0 0]
# 84005[3 1 0]<84013[0 0 0]
# 84005[3 2 0]<84013[0 0 0]
# 84005[4 -5 0]<84013[0 0 0]
# 84005[4 -4 0]<84013[0 0 0]
# 84005[4 -3 0]<84013[0 0 0]
# 84005[4 -2 0]<84013[0 0 0]
# 84005[4 -1 0]<84013[0 0 0]
# 84005[4 0 0]<84013[0 0 0]
# 84005[4 1 0]<84013[0 0 0]
# 84005[5 -5 0]<84013[0 0 0]
# 84005[5 -4 0]<84013[0 0 0]
# 84005[5 -3 0]<84013[0 0 0]
# 84005[5 -2 0]<84013[0 0 0]
# 84005[5 -1 0]<84013[0 0 0]
# 84005[5 0 0]<84013[0 0 0]
# ######################################################################## #
# in the MCNP, this card should be written as following:
# c rods' heat distribution in the most heated assembly(the middle one)
# F16:N  ((u=4)<94005[-5 0 0]<84013[0 0 0])
#        ((u=1)<94005[-5 1 0]<84013[0 0 0])
#        ((u=1)<94005[-5 2 0]<84013[0 0 0])
#        ((u=1)<94005[-5 3 0]<84013[0 0 0])
#        ((u=1)<94005[-5 4 0]<84013[0 0 0])
#        ((u=4)<94005[-5 5 0]<84013[0 0 0])
#        ((u=1)<94005[-4 -1 0]<84013[0 0 0])
#        ((u=1)<94005[-4 0 0]<84013[0 0 0])
#        ((u=1)<94005[-4 1 0]<84013[0 0 0])
#        ((u=1)<94005[-4 2 0]<84013[0 0 0])
#        ((u=1)<94005[-4 3 0]<84013[0 0 0])
#        ((u=1)<94005[-4 4 0]<84013[0 0 0])
#        ((u=1)<94005[-4 5 0]<84013[0 0 0])
#        ((u=1)<94005[-3 -2 0]<84013[0 0 0])
#        ((u=1)<94005[-3 -1 0]<84013[0 0 0])
#        ((u=9)<94005[-3 0 0]<84013[0 0 0])
#        ((u=3)<94005[-3 1 0]<84013[0 0 0])
#        ((u=3)<94005[-3 2 0]<84013[0 0 0])
#        ((u=9)<94005[-3 3 0]<84013[0 0 0])
#        ((u=1)<94005[-3 4 0]<84013[0 0 0])
#        ((u=1)<94005[-3 5 0]<84013[0 0 0])
#        ((u=1)<94005[-2 -3 0]<84013[0 0 0])
#        ((u=1)<94005[-2 -2 0]<84013[0 0 0])
#        ((u=3)<94005[-2 -1 0]<84013[0 0 0])
#        ((u=1)<94005[-2 0 0]<84013[0 0 0])
#        ((u=1)<94005[-2 1 0]<84013[0 0 0])
#        ((u=1)<94005[-2 2 0]<84013[0 0 0])
#        ((u=3)<94005[-2 3 0]<84013[0 0 0])
#        ((u=1)<94005[-2 4 0]<84013[0 0 0])
#        ((u=1)<94005[-2 5 0]<84013[0 0 0])
#        ((u=1)<94005[-1 -4 0]<84013[0 0 0])
#        ((u=1)<94005[-1 -3 0]<84013[0 0 0])
#        ((u=3)<94005[-1 -2 0]<84013[0 0 0])
#        ((u=1)<94005[-1 -1 0]<84013[0 0 0])
#        ((u=1)<94005[-1 0 0]<84013[0 0 0])
#        ((u=1)<94005[-1 1 0]<84013[0 0 0])
#        ((u=1)<94005[-1 2 0]<84013[0 0 0])
#        ((u=3)<94005[-1 3 0]<84013[0 0 0])
#        ((u=1)<94005[-1 4 0]<84013[0 0 0])
#        ((u=1)<94005[-1 5 0]<84013[0 0 0])
#        ((u=4)<94005[0 -5 0]<84013[0 0 0])
#        ((u=1)<94005[0 -4 0]<84013[0 0 0])
#        ((u=9)<94005[0 -3 0]<84013[0 0 0])
#        ((u=1)<94005[0 -2 0]<84013[0 0 0])
#        ((u=1)<94005[0 -1 0]<84013[0 0 0])
#        ((u=6)<94005[0 0 0]<84013[0 0 0])
#        ((u=1)<94005[0 1 0]<84013[0 0 0])
#        ((u=1)<94005[0 2 0]<84013[0 0 0])
#        ((u=9)<94005[0 3 0]<84013[0 0 0])
#        ((u=1)<94005[0 4 0]<84013[0 0 0])
#        ((u=4)<94005[0 5 0]<84013[0 0 0])
#        ((u=1)<94005[1 -5 0]<84013[0 0 0])
#        ((u=1)<94005[1 -4 0]<84013[0 0 0])
#        ((u=3)<94005[1 -3 0]<84013[0 0 0])
#        ((u=1)<94005[1 -2 0]<84013[0 0 0])
#        ((u=1)<94005[1 -1 0]<84013[0 0 0])
#        ((u=1)<94005[1 0 0]<84013[0 0 0])
#        ((u=1)<94005[1 1 0]<84013[0 0 0])
#        ((u=3)<94005[1 2 0]<84013[0 0 0])
#        ((u=1)<94005[1 3 0]<84013[0 0 0])
#        ((u=1)<94005[1 4 0]<84013[0 0 0])
#        ((u=1)<94005[2 -5 0]<84013[0 0 0])
#        ((u=1)<94005[2 -4 0]<84013[0 0 0])
#        ((u=3)<94005[2 -3 0]<84013[0 0 0])
#        ((u=1)<94005[2 -2 0]<84013[0 0 0])
#        ((u=1)<94005[2 -1 0]<84013[0 0 0])
#        ((u=1)<94005[2 0 0]<84013[0 0 0])
#        ((u=3)<94005[2 1 0]<84013[0 0 0])
#        ((u=1)<94005[2 2 0]<84013[0 0 0])
#        ((u=1)<94005[2 3 0]<84013[0 0 0])
#        ((u=1)<94005[3 -5 0]<84013[0 0 0])
#        ((u=1)<94005[3 -4 0]<84013[0 0 0])
#        ((u=9)<94005[3 -3 0]<84013[0 0 0])
#        ((u=3)<94005[3 -2 0]<84013[0 0 0])
#        ((u=3)<94005[3 -1 0]<84013[0 0 0])
#        ((u=9)<94005[3 0 0]<84013[0 0 0])
#        ((u=1)<94005[3 1 0]<84013[0 0 0])
#        ((u=1)<94005[3 2 0]<84013[0 0 0])
#        ((u=1)<94005[4 -5 0]<84013[0 0 0])
#        ((u=1)<94005[4 -4 0]<84013[0 0 0])
#        ((u=1)<94005[4 -3 0]<84013[0 0 0])
#        ((u=1)<94005[4 -2 0]<84013[0 0 0])
#        ((u=1)<94005[4 -1 0]<84013[0 0 0])
#        ((u=1)<94005[4 0 0]<84013[0 0 0])
#        ((u=1)<94005[4 1 0]<84013[0 0 0])
#        ((u=4)<94005[5 -5 0]<84013[0 0 0])
#        ((u=1)<94005[5 -4 0]<84013[0 0 0])
#        ((u=1)<94005[5 -3 0]<84013[0 0 0])
#        ((u=1)<94005[5 -2 0]<84013[0 0 0])
#        ((u=1)<94005[5 -1 0]<84013[0 0 0])
#        ((u=4)<94005[5 0 0]<84013[0 0 0])
# SD16 1 90R
