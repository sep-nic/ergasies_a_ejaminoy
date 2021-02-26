import re
from collections import Counter
#put your text file instead of keimeno12.txt
string = open('keimeno12.txt').read()
new_string = re.sub(r'[^a-zA-Z ]+', '', string)
open('b.txt', 'w').write(new_string)
list_arx=[]
list_arx[:0]=new_string
#switch to ascii characters
list_deyt = (list(map(str, map(ord, list_arx))))
#switch var to int
dok_list = [int(i) for i in list_deyt]
#keep the odd numbers only
dok_list = [i for i in dok_list if i % 2 == 1]
list_trt = [str(i) for i in dok_list]
listToStr = ' '.join(map(str, list_trt))
string_2 = (new_string.lower())
print (string_2)
k = len(string_2)
set = {}
for keys in string_2:
    #number of times a letter appears
    set[keys] = set.get(keys, 0) + 1
list_for=[]
list_for[:0]=string_2
final = list(set)
m = [0] * len(final)
#amount of times every letter is used
for i in range(0,len(final)):
        for j in range(0,len(list_for)):
            if final[i] == list_for[j]:
                m[i] = m[i]+1
print(' ')
pososto = "*"
for l in range(0,len(final)):
    p = ((m[l]/len(list_for))*100)

    q = int(p)

    if p != q:
        q = q+1

    print(final[l],":", pososto * q)
