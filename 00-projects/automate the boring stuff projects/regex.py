import re

number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = number.search('call me on 415-123-3231 please')
print(mo.group())
