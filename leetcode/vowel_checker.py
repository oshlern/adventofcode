# https://leetcode.com/problems/vowel-spellchecker/submissions/1808445513/
VOWELS = "aeiou"

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        return [self.spellcheck(wordlist, query) for query in queries]


    def spellcheck(self, wordlist: List[str], query: str):
        if query in wordlist:
            return query

        for word in wordlist:
            if self.same_up_to_capitalization(query, word):
                return word

        for word in wordlist:
            if self.same_up_to_vowels(query, word):
                return word

        return ""

    def same_up_to_capitalization(self, query, word):
        return query.lower() == word.lower()

    def same_up_to_vowels(self, query, word):
        if len(query) != len(word):
            return False
        for qc, wc in zip(query.lower(), word.lower()):
            if qc != wc and not (qc in VOWELS and wc in VOWELS):
                return False
        return True
