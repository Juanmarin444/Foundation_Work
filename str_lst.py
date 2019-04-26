# =FIND AND REPLACE= #

words = "It's thanksgiving day. It's my birthday,too!" 
### print words.find('day')
new_words = words.replace('day', 'month')
### print new_words

# =MIN AND MAX= #

x = [2,54,-2,7,12,98]
min = min(x)
max = max(x)
### print 'Min=> ', min
### print 'Max=> ', max

# =FIRST AND LAST= #

q = ["hello",2,54,-2,7,12,98,"world"]

### print q

new_q = [q[0], q[len(q) - 1]]
### print new_q

# =NEW LIST= #

x = [19,2,54,-2,7,12,98,32,10,-3,6]

sorted_list = [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]

def newList(lst):
    front_lst = []
    end_lst = []
    lst = sorted(lst)    

    j = 0
    while j < len(lst) / 2:
        # print lst[j]
        front_lst.append(lst[j])

        j += 1

    i = len(lst) - 1
    while i >= len(lst) / 2:
        # print i 
        end_lst.append(lst[i])

        i -= 1
        
    end_lst = sorted(end_lst)
    end_lst.insert(0,front_lst)
    print end_lst
newList(x)
