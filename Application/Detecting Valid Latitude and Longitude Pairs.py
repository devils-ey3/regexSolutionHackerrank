# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem
import re

for x in range(int(input())):
    if re.match('^\(([+-]?(90(\.0+)?|[1-8]?\d(\.\d+)?))\, ([+-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|[1-9]?\d(\.\d+)?))\)$',input()):
        print('Valid')
    else:
        print('Invalid')