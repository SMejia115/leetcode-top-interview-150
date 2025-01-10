from collections import Counter

class Solution:
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        max_freq = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char, freq in word_freq.items():
                max_freq[char] = max(max_freq[char], freq)
        
        
        result = []
        for word in words1:
            word_freq = Counter(word)
            if all(word_freq[char] >= freq for char, freq in max_freq.items()):
                result.append(word)
        
        return result