# https://www.hackerrank.com/challenges/hackerrank-tweets/problem
import re
count = 0
for x in range(int(input())):
    if re.search('(hackerrank)',input(),re.IGNORECASE):
        count+=1

print(count)
