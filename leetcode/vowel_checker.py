# https://leetcode.com/problems/vowel-spellchecker/submissions/1808445513/
VOWELS = "aeiou"
devowelize = lambda w: "".join("." if c in VOWELS else c for c in w.lower())

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ws = set()
        lws = dict()
        vws = dict()
        for w in wordlist:
            lw = w.lower()
            vw = devowelize(w)
            ws.add(w)
            if lw not in lws:
                lws[lw] = w
            if vw not in vws:
                vws[vw] = w

        return [q if q in ws else (l if (l := lws.get(q.lower())) else (v if (v := vws.get(devowelize(q))) else "")) for q in queries]
        # return [self.spellcheck(wordlist, query) for query in queries]


    def old_spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
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
