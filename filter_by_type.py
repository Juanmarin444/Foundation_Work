# INTERGER

def isBig(num):
    if num >= 100:
        print("That's a big number!")
    else:
        print("That's a small number!")

isBig(100)
isBig(99)
isBig(101)

print('====================')

# STRING

def isLong(string):
    if len(string) >= 50:
        print("That's a Long Sentence!", len(string))
    else:
        print("That's a Short Sentence!", len(string))
lngstr = '''
I like learning about different kinds of animals every day on educational 
Youtube channels, such as Animal logic ,and PBs Eons
 '''

isLong(lngstr)

isLong('I ate pizza today.')

print('====================')

# LIST  

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def isBigList(lst):
    if len(lst) >= 10:
        print("That's a big List.")
    else:
        print("That's a short List.")

# isBigList(sI)
# isBigList(mI)
# isBigList(bI)
# isBigList(eI)
# isBigList(spI)
isBigList(sS)
isBigList(mS)
isBigList(bS)
isBigList(eS)
isBigList(aL)
isBigList(mL)
isBigList(lL)
isBigList(eL)
isBigList(spL)