class Solution(object):
    def romanToInt(self, s):
        roman={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total=0
        previous=0
        for char in reversed(s):
            currentValue=roman[char]
            if currentValue<previous:
                total+=currentValue
            else:
                total+=currentValue
                previous=currentValue
        print(total)
            



