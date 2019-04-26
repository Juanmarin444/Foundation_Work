# MULTIPLES 
# PART ONE:

def showOdds(start, end):
    for x in range(start, end + 1):
        if x % 2 == 0:
            continue
        else:
            print x
showOdds(1, 100)

print '===================='

#PART TWO:  

def showMults(start, end, mult):
    for x in range(start, end + 1, mult):
        print x

showMults(5, 100, 5)

print '===================='

# SUM LIST 

a = [1, 2, 5, 10, 255, 3]
b = [3, 4, 6, 8, 33, 2, 1]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

def sumList(lst):
    sum = 0
    for x in lst:
        sum += x
    print sum

sumList(a)
sumList(b)
sumList(c)

print '===================='

# AVERAGE LIST
 
def avgList(lst):
    sum = 0.0
    
    for x in lst:
        sum += x

    avg = sum / len(lst)
    print(avg)

avgList(a)
avgList(b)
avgList(c)