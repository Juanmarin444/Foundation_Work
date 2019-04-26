

users = ['john', 'martin', 'andrew', 'daniel','tenzin','juan','charlie']
subscribed = ['yes','yes','no', 'yes','no']

# outcome = {
#     "john": "yes",
#     "martin": "yes",
#     "andrew": "no",
#     "daniel": "yes",
#     "tenzin": "no"
#     "unknown": "no"
#     "unknown": "yes"
# }

def make_dict(list1, list2):
    new_dict = {}

    if len(list1) > len(list2):
        long_list = list1
        short_list = list2
    else:
        long_list = list2
        short_list = list1

    differance = len(long_list) - len(short_list)

    for x in range(0, differance):
            short_list.append('unknown')
    
    i = 0
    while i < len(long_list):
        print long_list
        print short_list
        key = long_list[i]
        value = short_list[i]

        new_dict[key] = value
        
        i += 1

    print new_dict

make_dict(users,subscribed)

