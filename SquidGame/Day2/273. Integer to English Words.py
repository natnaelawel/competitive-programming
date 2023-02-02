class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        num = str(num)
        digits = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
        10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 
        18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 
        80: "Eighty", 90: "Ninety", 100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"}
        nums = list(str(num))
        vals = []
        i = 0
        rev_nums = nums[::-1]
        while i < len(nums):
            word = []
            for j in range(3):
                if i < len(nums):
                    word.append(rev_nums[i])
                    i += 1
            vals.append(word[::-1])
        vals = vals[::-1]
        res = []
        dig = len(vals)-1
        for i, curr_seg in enumerate(vals):
            curr_num = "".join(curr_seg)
            if int(curr_num) > 99 and len(curr_seg) == 3:
                res.append(digits[int(curr_num[0])])
                res.append(digits[100])
            if int(curr_num) <= 20:
                res.append(digits[int(curr_num)])
            else:
                if 20 < int(curr_num):
                    tenth_num = curr_num[1:] if len(curr_seg) == 3 else curr_num
                    tenth = int(tenth_num) - (int(tenth_num) % 10)
                    if tenth == int(tenth_num):
                        res.append(digits[int(tenth_num)])
                    else:
                        if int(tenth_num) <= 20:
                            res.append(digits[int(tenth_num)])
                        else:
                            res.append(digits[tenth])
                            res.append(digits[int(tenth_num) % 10])                     
            pow = 10 ** (3 * (dig-i))
            bet = digits[pow]
            if pow > 1 and int(curr_num) != 0:
                res.append(bet)
        res = [val for val in res if val != ""]
        return " ".join(res)  