# https://www.hackerrank.com/challenges/programming-language-detection/problem
import re
import sys

txt = sys.stdin.read()
if bool(re.search('#include ?<stdio.h>',txt,re.IGNORECASE)):
    print('C')
elif bool(re.search('import java',txt,re.IGNORECASE)):
    print('Java')
else:
    print('Python')