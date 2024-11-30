
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

"""
https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/?envType=company&envId=affirm&favoriteSlug=affirm-all

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # brute force solution O(n^2m^2) LOL 
        min_len = [2**31 - 1] * len(arr)
        result = [""] * len(arr)
        for i, s in enumerate(arr):
            # generate all substrings 
            substrs = []
            for start in range(len(s)):
                for L in range(1, len(s)+1):
                    substr = s[start: start+L]
                    substrs.append(substr)
            # maintain lexico order
            substrs.sort()
            for substr in substrs:
                found = False
                for j in range(len(arr)):
                    if i == j:
                        continue
                    # eliminate answer
                    if substr in arr[j]:
                        found = True
                        break
                if not found and len(substr) < min_len[i]:
                    min_len[i] = len(substr)
                    result[i] = substr
        return result
               
# Optimized solution                
 class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # More optimized solution: Count + Aggregate pattern
        # Count each substring subtstr: set(words)
        # Aggregate:
        # find the one with unique word, and output.

        # Edge case: ["fhi","ct","s","o","o"]
        # However if we have duplicated string, then the dup ones should have no answer 
        # So we just need to skip them
        word_to_index = defaultdict()
        result = [''] * len(arr)
        substrs_words = defaultdict(set)
        dups = set()
        # this step takes O(N * M^2)
        for i, word in enumerate(arr):
            if word in word_to_index:
                dups.add(word)
                continue
            word_to_index[word] = i
            # generate all substring
            for start in range(len(word)):
                for L in range(1, len(word) + 1):
                    substr = word[start: start + L]
                    substrs_words[substr].add(word)
        # aggregate result
        for substr, words in substrs_words.items():
            if len(words) == 1:
                # only count the unique ones
                word = list(words)[0]
                if word in dups:
                    continue
                index = word_to_index[word]
                if result[index] == '':
                    result[index] = substr
                elif len(substr) < len(result[index]):
                    result[index] = substr
                elif len(substr) == len(result[index]) and substr < result[index]: # lexico order
                    result[index] = substr
        return result                       
"""



if __name__ == '__main__':
    # test case 1
    words = ['cheapair', 'cheapoair', 'peloton', 'pelican']
    print (find_min_len_unique_substring(words))
    
    # test case 2
    words = ['abc', 'cde', 'dfg']
    print (find_min_len_unique_substring(words))
