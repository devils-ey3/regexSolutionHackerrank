# https://www.hackerrank.com/challenges/detect-html-links/problem
import re

for x in range(int(input())):
    x = re.findall(r'<a href="(.*?)".*?>([\w ,./]*)(?=</)',input())
    if not x==[]:
        for y in range(len(x)):
            print(','.join([z.strip() for z in x[y]]))