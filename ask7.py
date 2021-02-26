import requests
import datetime as dt

#apotelesmata teleytaion 10 klireseon kathe meras toy mina febroyarioy 2021



start_date = dt.datetime(2021, 2,1)
end_date = dt.datetime(2021, 2,28)

total_days = (end_date - start_date).days + 1 #inclusive 5 days

for day_number in range(total_days):
    current_date = (start_date + dt.timedelta(days = day_number)).date()
    print (current_date)

    #import results
    def get_winning_numbers(date: str, game_id: str = '1100'):
        url = f'https://api.opap.gr/draws/v3.0/{game_id}/draw-date/{date}/{date}'
        data = requests.get(url).json()
        winning_numbers = [game['winningNumbers']['list']
                       for game in data['content']]
        return winning_numbers

    print(get_winning_numbers(current_date))
    print(" ")
    #declaration of list with len 80
    a=list()
    b=list()
    for count in range(0,80):
        a.insert(count,count+1)
        b.insert(count,0)
    print(a)






    #amount of times a number is drawn
    print(" ")
    for i in range(0,10):
        k=get_winning_numbers(current_date)[i]
        for j in range(0,20):
            thesi=k[j]
            thesi2=thesi-1
            timi=b[thesi2]+1
            b[thesi2]=timi
    print(b)


    #most common number
    max=0
    thesi_max=0
    for i in range(0,80):
        if b[i]>max:
            max=b[i]
            thesi_max=i+1
    print(" ")
    print("Ο αριθμός που έχει κληρωθεί πιο πολλές φορές είναι το:",thesi_max)
    print(" ")
