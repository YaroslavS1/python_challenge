from typing import Counter
from urllib.request import urlopen
import collections

# скачиваем страницу
page = urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
contents = page.read().decode()
# выделяем из html зашифрованный код

s = contents.split('<!--')[2].split('-->')[0]
print(Counter(s))


 