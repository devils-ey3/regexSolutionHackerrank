# https://www.hackerrank.com/challenges/uk-and-us/problem
import re
lst = []
for x in range(int(input())):
    lst.append(input())
string = '\n'.join([x for x in lst])
for x in range(int(input())):
    regex = re.compile(str(input()[:-2])+'[zs]e',re.IGNORECASE)
    words = regex.finditer(string)
    print(len(list(words)))