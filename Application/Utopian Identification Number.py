# https://www.hackerrank.com/challenges/utopian-identification-number/problem


import re
count = 0
for x in range(int(input())):
    if re.search('^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$',input()):
        print('VALID')
    else:
        print("INVALID")