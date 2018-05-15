# https://www.hackerrank.com/challenges/html-attributes/problem
import re
from collections import OrderedDict
lst = []
for x in range(int(input())):
    lst.append(input())
string = '\n'.join([x for x in lst])
dict_x = OrderedDict()
for tag,attr in sorted(re.findall('<(\w+)(\s+[^>]*|)>',string,re.IGNORECASE)):
    dict_x.setdefault(tag, []).append(attr.strip())
attributes = set()
for key,value in dict_x.items():
    print(key,end=':')
    for x in value:
        for y in re.findall('(\w+)?=[\'\"].*?[\'\"]',x):
            attributes.add(y)
    print(','.join([x for x in sorted(attributes)]))
    attributes.clear()