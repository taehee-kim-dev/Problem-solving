import re

p = re.compile('/^123$/')
result = p.match('123')
if result is None:
    print('매치 안됨')
else:
    print('매치됨')