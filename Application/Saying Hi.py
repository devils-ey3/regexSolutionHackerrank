# https://www.hackerrank.com/challenges/saying-hi/problem
import re
for x in range(int(input())):
    text = input()
    if re.search('^hi [^d].+$',text,re.IGNORECASE):
        print(text)