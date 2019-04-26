words = ['Hello','world','my','name','is','Juan.']
character = 'j'

def findChar(word_lst, char):
    new_list = []
    lc_char = char.lower()
    for word in word_lst:
        lc_word = word.lower()
        for letter in lc_word:
            if letter == lc_char:
                new_list.append(word)

    return new_list

print(findChar(words, character))