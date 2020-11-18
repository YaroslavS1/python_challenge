from urllib.request import urlopen

nothing = '12345'
www = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

final = []
for i in range(0, 400):
    nothing = urlopen(www + nothing).read().decode().split(' ')[-1]
    print(nothing)
    final.append(nothing)

final_final = [x for x in final if not x.isdigit()]
print(final_final)
