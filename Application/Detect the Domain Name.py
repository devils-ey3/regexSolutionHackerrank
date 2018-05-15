# https://www.hackerrank.com/challenges/detect-the-domain-name/problem
import re

lst = []
for x in range(int(input())):
    lst.append(input())
lst = '\n'.join([x for x in lst])

email = re.findall('https?:\/\/(?:www.|ww2.)?([a-zA-Z\-0-9\.]+\.[a-zA-Z\-0-9\.]+)',lst)

print(';'.join([x for x in sorted(set(email))]))