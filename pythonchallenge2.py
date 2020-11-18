from typing import Counter
from urllib.request import urlopen
import collections

# скачиваем страницу
page = urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
contents = page.read().decode()
# выделяем из html зашифрованный код

s = contents.split('<!--')[1].split('-->')[0]
# print(s)
 
# с регулярными выражениями всё становится проще
import re
r = re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
print(''.join(re.findall(r, s)))


 