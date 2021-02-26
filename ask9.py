import re
from collections import Counter
#put your text file instead of keimeno12.txt
string = open('keimeno12.txt').read()
new_str = re.sub(r'[^a-zA-Z ]+', '', string)
open('b.txt', 'w').write(new_str)
list1=[]
list1[:0]=new_str
#switch to ascii characters
list2 = (list(map(str, map(ord, list1))))
#switch var to int
test_list = [int(i) for i in list2]
#keep the odd numbers only
test_list = [i for i in test_list if i % 2 == 1]
list3 = [str(i) for i in test_list]
listToStr = ' '.join(map(str, list3))
string2 = (new_str.lower())
print (string2)
z = len(string2)
res = {}
for keys in string2:
    #number of times a letter appears
    res[keys] = res.get(keys, 0) + 1
listfor=[]
listfor[:0]=string2
finalist = list(res)
l = [0] * len(finalist)
#amount of times every letter is used
for i in range(0,len(finalist)):
        for j in range(0,len(listfor)):
            if finalist[i] == listfor[j]:
                l[i] = l[i]+1
print(' ')
pososto = "*"
for p in range(0,len(finalist)):
    s = ((l[p]/len(listfor))*100)

    g = int(s)

    if s != g:
        g = g+1

    print(finalist[p],":", pososto * g)
