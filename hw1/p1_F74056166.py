# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:32:59 2019

@author: 方嘉祥
"""

from functions import func
import sys

a = sys.argv
f = open(a[1], "r")
w = open(a[2], "w")
x_position_range = f.readline()
x_range = x_position_range.split(',')
x_range = [int(i) for i in x_range]
print(x_range)

y_position_range = f.readline()
y_range = y_position_range.split(',')
y_range = [int(i) for i in y_range]
print(y_range)


bully_count = 0
bully_min = 9999999999

for x in range(x_range[0], x_range[1]+1):
    for y in range(y_range[0], y_range[1]+1):
        z = func(x, y)
        bully_count += 1
        if z < bully_min:
            bully_min = z

print('bully_min: ' + str(bully_min))
print('bully count: ' + str(bully_count))
w.write("%.3f" % bully_min)
w.write('\n')


initial_position_num = int(f.readline())
print(initial_position_num)
stepsize = 1
for i in range(initial_position_num):
    initial_point = f.readline();
    initial_point = initial_point.split(',')
    initial_point = [int(i) for i in initial_point]
    print(initial_point)

    point_x = initial_point[0]
    point_y = initial_point[1]
    print('x:' + str(point_x) + ' y:' + str(point_y))
    start_min = func(point_x, point_y)
    
    hill_count = 0

    while 1:
        way = [99999, 99999, 99999, 99999]
        up_way = 99999
        down_way = 99999
        left_way = 99999
        right_way = 99999
        if point_y + stepsize <= y_range[1]:
          way[0] = func(point_x, point_y + stepsize)
          
        if point_y - stepsize >= y_range[0]:
          way[1] = func(point_x, point_y - stepsize)
          
        if point_x - stepsize >= x_range[0]:
          way[2] = func(point_x - stepsize, point_y)
          
        if point_x + stepsize <= x_range[1]:
          way[3] = func(point_x + stepsize, point_y)
        hill_count += 4
        if start_min >= min(way):
            start_min = min(way)
            if way.index(min(way)) is 0:
                point_y = point_y + stepsize
            elif way.index(min(way)) is 1:
                point_y = point_y - stepsize
            elif way.index(min(way)) is 2:
                point_x = point_x - stepsize
            elif way.index(min(way)) is 3:
                point_x = point_x + stepsize
        else:
            print("%.3f" % start_min)
            print('count: ' + str(hill_count))
            w.write("%.3f" % start_min)
            w.write('\n')
            break
        
f.close()
w.close()
