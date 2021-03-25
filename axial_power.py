#!/usr/bin/env python
#! -*- coding:utf-8 -*-

index = 0

with open("core1o", 'r') as f:
    lines = f.readlines()
    for each_line in lines:
        if ' cell (1<4014)' in  each_line:
            index = lines.index(each_line)

result = [lines[index+i].strip().split()[0] for i in range(1, 1501, 3)]
result = '\n'.join(result)

with open("fuck.txt", 'w') as f:
    f.write(result)
    
print("Done!")