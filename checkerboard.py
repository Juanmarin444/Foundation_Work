
def drawBoard():

    for row in range(5):
        print 'row', row,
        for col in range(5):
            print 'col', col,
           
            offset = 0
            if row % 2 == 0:
                offset = 1

            if (col + offset) % 2 == 0:
                print '@',
            else:
                print '*',
        print ""

# , <= a comma can be used to print in rows
drawBoard()
