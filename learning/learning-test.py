import re


test = '123asdf123'

return_test = re.sub('123', '', test)

print('test : {}', test)
print('return_test : {}', return_test)
