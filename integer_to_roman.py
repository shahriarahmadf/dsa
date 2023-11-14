class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {
            1: 'I',
            
            4: 'IV',
            5: 'V',

            9: 'IX',
            10: 'X',

            40: 'XL',
            50: 'L',

            90: 'XC',
            100: 'C',

            400: 'CD',
            500: 'D',

            900: 'CM',
            1000: 'M'
        }

        keys = []
        for key in hashmap.keys():
            keys.append(key)
        keys.reverse()
        roman = ''
        key_no = 0
        while key_no < len(keys) and num > 0:
            if keys[key_no] <= num:
                roman += hashmap[keys[key_no]]
                num -= keys[key_no]
            else:
                key_no += 1
        return roman