'''
divid by 2 if whole false
if whole divide by prime numbers
if the output is a whole number then it is not a prime number
'''

def foobar(start, end):

    # iterate through the numbers we want to check.
    for num in range(start, end + 1):
        
        # if the number we are looking at specifically (num) is less the one
        # print Not a Prime number.
        if num < 1:
            print("Not Prime", num)

        # iterate through the numbers between 2 and (num)
        for j in range(2, num):

            # multiply each number (j) with itself and check
            # to see if their product is equal to the value of (num)
            # if it is equal then print 'bar'
            if j * j == num:
                print('Bar!', num)

        # iterate through the numbers between 2 and (num)        
        for i in range(2, num):

            # divide num by each (i) to see if their quotient is a
            # whole number. if it is a whole number then just skip
            # to the next number.
            if num % i == 0:
                break

        # if all of the conditionals above fail then the number (num)
        # is a prime number and print 'foo'
        else:
            print('Foo!', num)

foobar(1,423)
