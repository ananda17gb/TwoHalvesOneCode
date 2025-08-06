class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        stringified = "".join(map(str, digits))
        plus_one = int(stringified) + 1
        string_plus_one = str(plus_one)
        result = []
        for i in string_plus_one:
            result.append(int(i))
        return result
