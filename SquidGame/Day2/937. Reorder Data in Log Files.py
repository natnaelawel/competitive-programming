from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            logs_vals = log.split(" ")
            ident, vals = logs_vals[0], logs_vals[1:]
            if  ord("a") <= ord(vals[0][0].lower()) <= ord("z"):
                letter_logs.append((ident, vals))
            else:
                digit_logs.append((ident, vals))

        letter_logs = sorted(letter_logs, key= lambda x: (" ".join(x[1]), x[0]))
        res = [" ".join([log[0]] + log[1]) for log in letter_logs+digit_logs]
        return  res