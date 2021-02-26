import tweepy
import re

#Import credentials from keyboard
cons_k = input("Παρακαλώ εισαγέτε το consumer key:\n")
print(f'Εισάγατε {cons_k}')
print(" ")
cons_s = input("Παρακαλώ εισαγέτε το consumer secret:\n")
print(f'Εισάγατε {cons_s}')
print(" ")
acs_k = input("Παρακαλώ εισαγέτε το access token key:\n")
print(f'Εισάγατε {acs_k}')
print(" ")
acs_s = input("Παρακαλώ εισαγέτε το access token secret:\n")
print(f'Εισάγατε {acs_s}')
print(" ")



#Setup access to API
auth = tweepy.OAuthHandler(cons_k,cons_s)
auth.set_access_token(acs_k,acs_s)
api = tweepy.API(auth)


#insert username
user_name = input("Please enter username:\n")
print(f'You entered {user_name}')


tweets = api.user_timeline(screen_name=user_name, count = 200, include_rts = False ,tweet_mode = 'extended')


list1 = []
i=0
#last 10 tweets
for mes in tweets[:10]:
     i = i + 1
     print(i)
     print(mes.created_at)
     print(mes.full_text)
     #convert tweets into list
     list1.append(mes.full_text)
     print("\n")
print(list1)
print(" ")
#list into string
str1=" "
str1 = str1.join(list1)
#remove url
str1 = re.sub(r"http\S+", "", str1)
#remove mentions
str1=re.sub("@[_A-Za-z0-9]+","",str1)
#remove punctiation
str1 = re.sub("[^Α-Ωα-ωάίύόήώέϊϋΐΰΪΫA-Za-z]+", " ", str1)
str1=str1.lower()
print(str1)
print(" ")
#every word of string into differt position of list
wordlist = str1.split()
print(wordlist)
#declaeation of lists
megalytero=[]
mikrotero=[]
for x in range(0,5):
    megalytero.append(wordlist[x])
    mikrotero.append(wordlist[x])
#table of 5 biggest words
for k in range(5,len(wordlist)):
    min=len(megalytero[0])
    thesi_min=0
    for l in range(0,5):
        if len(megalytero[l])<min:
            min=len(megalytero[l])
            thesi_min=l
    if len(wordlist[k])>min:
        if wordlist[k] not in megalytero:
            del megalytero[thesi_min]
            megalytero.insert(thesi_min,wordlist[k])
print(" ")
print("Οι 5 μεγαλύτερες λέξεις είναι: ")
print(megalytero)
#table of 5 smallest words
for m in range(5,len(wordlist)):
    max=len(mikrotero[0])
    thesi_max=0
    for n in range(0,5):
        if len(mikrotero[n])>max:
            max=len(mikrotero[n])
            thesi_max=n
    if len(wordlist[m])<max:
        if wordlist[m] not in mikrotero:
            del mikrotero[thesi_max]
            mikrotero.insert(thesi_max,wordlist[m])
print(" ")
print("Οι 5 μικρότερες λέξεις είναι: ")
print(mikrotero)
