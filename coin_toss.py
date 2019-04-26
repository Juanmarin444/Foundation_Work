import random

def coin_tossing():
    tails = 0
    heads = 0

    for toss in range(200):
        random_num = random.random()
        rounded_num = round(random_num)
        if rounded_num == 1:
            tails += 1
            print "It's tails! ... got ", tails, " tail(s) and ", heads," head(s) so far!"
            continue

        elif rounded_num == 0:
            heads += 1
            print "It's heads! ... got ", tails, " tail(s) and ", heads," head(s) so far!"
            continue            

coin_tossing()