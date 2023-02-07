from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        ans = []
        lines = []
        while i < len(words):
            line = [list(words[i])]
            letter_size = len(words[i])
            len_word = len(words[i])
            j = i+1
            while j < len(words) and (letter_size + 1 + len(words[j])) <= maxWidth:
                word = list(words[j])
                line.append(word)
                len_word += len(word)
                letter_size += len(word) + 1
                j += 1
            i = j
            lines.append([line, len_word])
        for i in range(len(lines)-1):
            line, len_word = lines[i]
            if len(line) == 1:
                line[0].extend([" "] * (maxWidth - len_word))
            else:
                sp_full = (maxWidth - len_word) // (len(line)-1)
                sp_rem = (maxWidth - len_word) % (len(line)-1)
                for k in range(len(line)-1):
                    line[k].extend([" "] * (sp_full + (1 if k < sp_rem else 0)))
            ans.append("".join(["".join(word) for word in line]))
        line, len_word = lines[-1]
        last_line = " ".join(["".join(word) for word in line] )
        last_line += "".join([" "] * (maxWidth - len(last_line)))
        ans.append(last_line)
        return ans


sol = Solution()
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["What","must","be","acknowledgment","shall","be"]
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
maxWidth = 16
print(sol.fullJustify(words, 20))
            
                