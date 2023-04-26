class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words_with_index = [(word[:-1], int(word[-1])) for word in words]
        words_with_index.sort(key=lambda x: x[1])
        original_sentence = " ".join([word for word, _ in words_with_index])
    
        return original_sentence
