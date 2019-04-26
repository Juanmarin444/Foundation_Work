users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def read(obj):

    for data in obj:
        people = obj[data]
        print data
        count = 0
        
        for students in people:
            count += 1
            f_len = len(students['first_name'])
            l_len = len(students['last_name'])
            t_len = f_len + l_len
            print count, students['first_name'], students['last_name'], t_len

read(users)