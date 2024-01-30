import random as rn

word1 = 'word'
word2 = 'lol'
print(word1 == word1[::-1], word2 == word2[::-1])
print(word1 is word1[::-1], word2 is word2[::-1])


def is_palindrome(word):
    return word == word[::-1]

def invert(dict_given):
    dict_inv = {value: key for (key, value) in dict_given.items()}
    return dict_inv

test_dict = {'a': 1, 'b' : 2, 'c': 3}

inv_dict = invert(test_dict)

print(inv_dict)


def spongecase(text):
    spongetext = ''
    for i in range(len(text)):
        if rn.randint(1,100) % 2 == 0:
            spongetext += text[i].upper()
        else:
            spongetext += text[i]

    return spongetext

print(spongecase('Using SpongeBob memes does not make you witty'))