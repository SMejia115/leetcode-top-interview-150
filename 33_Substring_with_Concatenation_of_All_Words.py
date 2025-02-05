import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        word_freq = collections.Counter(words)
        res = []
        
        # Se itera para cada offset (0 a word_len - 1)
        for i in range(word_len):
            left = i      # marca el inicio de la ventana actual
            count = 0     # cantidad de palabras válidas en la ventana actual
            cur_freq = {}
            
            # Se mueve el puntero j en saltos de word_len
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                
                if word in word_freq:
                    cur_freq[word] = cur_freq.get(word, 0) + 1
                    count += 1
                    
                    # Si tenemos demasiadas ocurrencias de 'word', mover el puntero left para ajustarlas
                    while cur_freq[word] > word_freq[word]:
                        left_word = s[left:left+word_len]
                        cur_freq[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # Si el número de palabras coincide con total_words, se encontró un concatenado válido
                    if count == total_words:
                        res.append(left)
                        # Mover left un paso para buscar nuevas posibilidades
                        left_word = s[left:left+word_len]
                        cur_freq[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # Reiniciar la ventana si la palabra actual no está en la lista de words
                    cur_freq.clear()
                    count = 0
                    left = j + word_len
        
        return res