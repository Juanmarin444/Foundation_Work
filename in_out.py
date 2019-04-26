# function input
my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
    }

# function output = [
#     ("Speros", "(555) 555-5555"),
#     ("Michael", "(999) 999-9999"),
#     ("Jay", "(777) 777-7777")
# ]

def in_out(obj):
    lst_tple = []
    for key in obj:
        tple = (key, obj[key])
        lst_tple.append(tple)
    return lst_tple

print in_out(my_dict)