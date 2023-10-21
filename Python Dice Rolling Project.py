import random

rolls=int(input('how many times do you want to roll?'))
sides=int(input('How many sides is your dice'))
for counter in range (rolls):
        randomDice = random.randrange(sides)+1
        print(randomDice)
        if randomDice==20:
                print('critical hit')
        if randomDice==1:
                print('critical miss')

print('done rolling')

#https://www.youtube.com/watch?v=8TNEtpt1gHU 
