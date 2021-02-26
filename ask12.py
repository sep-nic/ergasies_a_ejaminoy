import re
#import text file
#switch keimeno12.txt with your file
string = open('keimeno12.txt').read()
print(string)
print(" ")
len_str=len(string)
#reverse characters and find mirror characters
for i in range(len_str,1,-1):
    ascii_num=ord(string[i-1])
    mirror_num=128-ascii_num
    katoptrikos=chr(mirror_num)
    print(string[i-1],":",katoptrikos)
