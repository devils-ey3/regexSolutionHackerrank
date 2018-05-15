# https://www.hackerrank.com/challenges/valid-pan-format/problem
import re
count = 0
for x in range(int(input())):
    if re.search('^[A-Z]{5}[0-9]{4}[A-Z]$',input()):
        print('YES')
    else:
        print("NO")
