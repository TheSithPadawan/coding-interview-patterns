
from collections import defaultdict

"""
I am an affirm user and I would like to search for one of my fav merchants
Suppose I can type in a string and the app shows all merchants match that string
I want to type the shortest string possible to uniquely match each
merchant name.

Given a list of names for each name find the shortest substring that only
appears in that name.
https://www.1point3acres.com/bbs/thread-832960-1-1.html
"""
def find_min_len_unique_substring(words):
    result = dict()
    substr_to_words = defaultdict(list)
    # generate substring and update count
    for w in words:
        # enumerate all possible length
        for L in range(1, len(w) + 1):
            for start in range(len(w)):
                substr = w[start: start+L]
                if len(substr) == L:
                    substr_to_words[substr].append(w)

    # check result
    for k, v in substr_to_words.items():
        # unique one
        if len(v) == 1:
            if v[0] not in result:
                result[v[0]] = k
            else:
                # update to the min len substring
                if len(k) < len(result[v[0]]):
                    result[v[0]] = k
        
    return result



if __name__ == '__main__':
    # test case 1
    words = ['cheapair', 'cheapoair', 'peloton', 'pelican']
    print (find_min_len_unique_substring(words))
    
    # test case 2
    words = ['abc', 'cde', 'dfg']
    print (find_min_len_unique_substring(words))
