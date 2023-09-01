class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # find the largest binary number digit size
        largest = max(len(a),len(b))

        # make the smaller digit sized binary to equal sized binary by adding zeros to the left
        if largest == len(a):
            b = str(0)*(largest-len(b)) + b
        else:
            a = str(0)*(largest-len(a)) + a

        ans = ''
        carry = 0

        # a loop that runs from the right most index of the binary numbers (both are now same digit sized)
        for i in range(-1,-(largest+1),-1):
            add = int(a[i]) + int(b[i]) + carry
            carry = 0

            if add == 2:
                add = 0
                carry = 1
            if add == 3:
                add = 1
                carry = 1

            ans = str(add) + ans
        if carry == 1:
            ans = str(carry) + ans
        return ans