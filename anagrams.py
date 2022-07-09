# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


def anagrams(word, words):
    res = []
    len_word = len(word)
    for i in words:
        if len_word == len(i):
            res.append(i)

    res_index = []
    for i in range(len(res)):
        for j in res[i]:
            if j not in word:
                res_index.append(i)
                break

    res_new = []
    for i in range(len(res)-1):
        if i not in res_index:
            res_new.append(res[i])

    return res_new


word = 'abba'
words = ['aabb', 'abcd', 'bbaa', 'dada', 'sdfs']
print(anagrams(word, words))
