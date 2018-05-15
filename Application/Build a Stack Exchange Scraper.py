# https://www.hackerrank.com/challenges/stack-exchange-scraper/problem

import re
import sys

pat = '<a href="\/questions\/(\d+).+?">(.*?)<\/.*?(?:class\=\"relativetime\"\>)(.+?)<\/'
txt = sys.stdin.read()
for x in re.findall(pat, txt, re.DOTALL|re.MULTILINE):
    print(';'.join([y for y in x]))