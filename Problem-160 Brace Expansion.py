# 1087. Brace Expansion
# https://leetcode.com/problems/brace-expansion/

# Logic: Covert the input into list of lists. Recurse over the processed list and backtrack.

# Time Complexity: O(k^(n/k)) [k is the avg length of words inside braces and n is the total length]
# Space Complexity: O(n)

class Solution:
    def _helper(self, blocks, idx, curPath, result):
        # Base Case
        if idx == len(blocks):
            result.append("".join(curPath))
            return
        
        for j in range(len(blocks[idx])):
            curPath.append(blocks[idx][j])

            self._helper(blocks, idx + 1, curPath, result)

            curPath.pop()

    def expand(self, s: str):
        # Preprocess: Convert input into list of list
        blocks = []
        i = 0

        while i < len(s):
            temp = []
            if s[i] == '{':
                i += 1
                while s[i] != '}':
                    if s[i] != ',':
                        temp.append(s[i])
                    i += 1
            else:
                temp.append(s[i])
            blocks.append(temp)
            i += 1
        
        result = []
        self._helper(blocks, 0, [], result)

        return result


obj = Solution()
print(obj.expand('{a,b}c{d,e}f'))
print(obj.expand('abcde'))