class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 201
        length = 201
        for word in strs:
            length = len(word)
            min_length = min(length,min_length)
        index = 0
        arr = []
        final_arr = ""
        while min_length > 0:
            for word in strs:
                arr.append(word[index])
            index += 1
            min_length -= 1

            if all(element == arr[0] for element in arr):
                final_arr += arr[0]
                arr = []
            else:
                return final_arr
        return final_arr

# another solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res