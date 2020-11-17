from googletrans import Translator

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
raw_1 = "map"

def desckription(char):
    if 'a' <= char <= 'z':
        t = ord(char) + 2
        t = (t - ord('a')) % 26
        c = chr(t + ord('a'))
        return c
    else:   
        return char

result = ''
for c in raw:
    result += desckription(c)

print(result)

translator = Translator()
result_rus = translator.translate(result, src='en', dest='ru')

print(result_rus.text)
