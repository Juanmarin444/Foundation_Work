
lst1 = ['cow',1,'cow',1,'cow']
lst2 = ['cow',0,'cow',0,'cow']
lst3 = ['',1,'',1,'']
lst4 = ['',0,'',0,'']
lst5 = [1,1,1,1,1,1]
lst6 = [0,0,0,0,0,0]
lst7 = ['cow','cow']
lst8 = ['','']

def typeSort(lst):
    zeros = 0
    sum = 0
    sentence = ''
    empty_str = 0

    for ele in lst:
        if type(ele) == int:
            if ele == 0:
                zeros += 1
            sum += ele

        if type(ele) == str:
            if len(ele) > 0:
                sentence += ele
            elif len(ele) == 0:
                empty_str += 1

    if sum > 0 and len(sentence) > 0: # nums and strs
        print("The list you entered contains nums and strs.")
        print sum
        print sentence    

    if sum == 0 and len(sentence) > 0 and zeros > 0: # nums(0) and strs
        print("The list you entered contains nums(0) and strs.")
        print sum
        print sentence

    if sum == 0 and len(sentence) == 0 and zeros > 0 and empty_str > 0: # nums(0) and strs(0)
        print('The list you entered contains strs(0) and nums(0)')
        print sum
        print sentence    

    if sum > 0 and len(sentence) == 0 and empty_str > 0: # nums and strs(0)
        print("The list you entered contains nums and strs(0).")
        print sum
        print sentence    

    if sum > 0 and len(sentence) == 0 and empty_str == 0: # nums
        print("The list you entered is of INT type.")
        print sum
        print sentence    

    if sum == 0 and len(sentence) == 0 and zeros > 0 and empty_str == 0: # nums(0)
        print("The list you entered is of INT Type nums were all 0.")
        print sum
        print sentence    

    if sum == 0 and len(sentence) > 0 and zeros == 0: # str
        print("The list you entered is of str type.")
        print sum
        print sentence    

    if sum == 0 and len(sentence) == 0 and zeros == 0 and empty_str > 0: # str(0)
        print ('The list you entered is of str type with all str size 0') 
        print sum
        print sentence    

 

print('============== list 1', 'nums / strs')
typeSort(lst1)
print('============== list 2', 'nums(0) / strs')
typeSort(lst2)
print('============== list 3', 'nums / strs(0)')
typeSort(lst3)
print('============== list 4', 'nums(0) / strs(0)')
typeSort(lst4)
print('============== list 5', 'nums')
typeSort(lst5)
print('============== list 6', 'nums(0)')
typeSort(lst6)
print('============== list 7', 'strs')
typeSort(lst7)
print('============== list 8', 'strs(0)')
typeSort(lst8)



