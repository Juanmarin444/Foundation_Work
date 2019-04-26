def iMultTable():
    n=int(input('Please enter a positive integer between 1 and 15: '))
    for row in range(1,n+1):
        for col in range(1,n+1):
            print row * col,
        print('')

# iMultTable()

def testInput():
    juan = 'juan'
    marin = 'marin'
    first_name = str(input('Please enter your First Name here: '))
    last_name = str(input('Please enter your Last Name here: '))
    
    print 'my name is ', first_name, last_name

# testInput()

def multTable(num):

    for row in range(1, num + 1):
        for col in range(1, num + 1):
            print row * col,
        print ''

multTable(3)
multTable(12)