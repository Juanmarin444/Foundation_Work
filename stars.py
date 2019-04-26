
stars = [4, 3, 6, 2, 6]
stars_two = [4, 2, 'cow', 'sick', 6]

def draw_stars(arr):

    for ele in arr:
        if type(ele) == int:

            for value in range(1, ele + 1 ):
            
                print '*',
            
        elif type(ele) == str:
            for string in range(len(ele)):

                print ele[0],
        print ''

draw_stars(stars)
draw_stars(stars_two)
