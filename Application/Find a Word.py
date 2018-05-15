# https://www.hackerrank.com/challenges/find-a-word/problem
import re
lst = []
for x in range(int(input())):
    lst.append(input())
lst = '\n'.join([x for x in lst])
for x in range(int(input())):

    z = re.findall("(^|(?<=\W))" + input() + "(?=\W)",lst)
    print(len(z))