# https://www.hackerrank.com/challenges/detect-html-tags/problem
import re
set = set()
for x in range(int(input())):
    x = re.findall(r'< *?([\w]+) ?',input())
    if not x==[]:
        for y in x:
            set.add(y)

print(';'.join(x for x in sorted(set)))