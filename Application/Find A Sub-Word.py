# https://www.hackerrank.com/challenges/find-substring/problem
import re
set = set()
lst = []
for x in range(int(input())):
    lst.append(input())
lst = '\n'.join([x for x in lst])
for x in range(int(input())):
    z = re.findall(r'\B'+input()+'\B',lst)
    print(len(z))