me = {
    "first_name": "Juan",
    "last_name": "Marin",
    "age": 22,
    "cob": "Guatemala",
    "fav_lang": "python"
}

def auto_bio(arr):
    print "My name is", arr["first_name"], arr['last_name']
    print "I'm", arr["age"]
    print "I was born in", arr['cob'], "and"
    print "my favorite language is", arr["fav_lang"]

auto_bio(me)