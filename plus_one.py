class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        place = len(digits)-1
        while place>=0:
            print(digits[place])
            if digits[place] == 9:
                digits[place] = 0
            else:
                digits[place] += 1
                return digits
            place -= 1

        new_digits = [1]
        for digit in digits:
            new_digits.append(digit)
        return new_digits
        