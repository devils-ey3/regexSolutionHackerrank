# https://www.hackerrank.com/challenges/detect-the-email-addresses/problem
import re

lst = []
for x in range(int(input())):
    lst.append(input())
lst = '\n'.join([x for x in lst])

email = re.findall('(\S+@\S+\.\w*\w)',lst)

print(';'.join([x for x in sorted(set(email))]))