# https://www.hackerrank.com/challenges/alien-username/problem
import re

for x in range(int(input())):
    z = bool(re.search('^(?:_|\.)\d+[a-zA-Z]*_?$',input()))
    print(['INVALID','VALID'][z])