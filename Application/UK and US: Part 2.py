# https://www.hackerrank.com/challenges/uk-and-us-2/problem
import re
lst = []
for x in range(int(input())):
    lst.append(input())
string = '\n'.join([x for x in lst])
for x in range(int(input())):
    expression = re.sub('our','o[u]?r',input())
    regex = re.compile('\\b'+expression+'\\b',re.IGNORECASE)
    words = regex.finditer(string)
    print(len(list(words)))
