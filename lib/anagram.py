class Anagram:
    def __init__(self, word):
        self.word = word.lower()  
        self.sorted_word = sorted(self.word)

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            normalized = candidate.lower()
            if normalized != self.word and sorted(normalized) == self.sorted_word:
                matches.append(candidate)  
        return matches
