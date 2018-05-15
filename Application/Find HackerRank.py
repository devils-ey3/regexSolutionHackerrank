# https://www.hackerrank.com/challenges/find-hackerrank/problem
import re
for x in range(int(input())):
    text = input()
    if text.startswith('hackerrank') and text.endswith('hackerrank'):
        print('0')
    elif text.startswith('hackerrank') :
        print('1')
    elif text.endswith('hackerrank') :
        print('2')
    else:
        print('-1')