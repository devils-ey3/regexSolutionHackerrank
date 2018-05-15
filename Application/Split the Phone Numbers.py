# 
import re
for x in range(int(input())):
    y =  re.findall('^(\d{1,3})[-\s](\d{1,3})[-\s](\d{4,10})$',input())[0]
    print('CountryCode='+str(y[0])+',LocalAreaCode='+str(y[1])+',Number='+str(y[2]))