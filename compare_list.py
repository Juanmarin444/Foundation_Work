list_a = [1,2,5,6,2]
list_b = [1,2,5,6,2]

list_c = [1,2,5,6,5]
list_d = [1,2,5,6,5,3]

list_e = [1,2,5,6,5,16]
list_f = [1,2,5,6,5]

list_g = ['celery','carrots','bread','milk']
list_h = ['celery','carrots','bread','cream']


def isIdentical(list_one, list_two):
    if len(list_one) != len(list_two):
        return 'false'

    i = 0
    while i < len(list_one):

        if list_one[i] != list_two[i]:
            return 'false'
        else:
            i += 1
            continue
        i += 1
    return 'true'

print(isIdentical(list_a, list_b))
print(isIdentical(list_c, list_d))
print(isIdentical(list_e, list_f))
print(isIdentical(list_g, list_h))