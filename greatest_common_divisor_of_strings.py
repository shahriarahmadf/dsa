class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        prefixes = []
        str2_size = len(str2)
        prefix = ''
        for i in str2:
            prefix += i

            prefix_size = len(prefix)


            if str2_size % prefix_size == 0:
                times = str2_size / prefix_size

                substr = ''
                for i in range(int(times)):
                    substr += prefix

                    if substr == str2:
                        str1_size = len(str1)

                        if str1_size % prefix_size == 0:
                            times = str1_size / prefix_size

                            substr = ''
                            for i in range(int(times)):
                                substr += prefix

                                if substr == str1:
                                    prefixes.append(prefix)
        if len(prefixes) > 0:
            return max(prefixes)
        else:
            return ""