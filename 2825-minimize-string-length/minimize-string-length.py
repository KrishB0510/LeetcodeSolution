class Solution:
    def minimizedStringLength(self, s: str) -> int:
        hash_table={}
        for i in s:
            if i not in hash_table:
                hash_table[i]=1
        return len(hash_table)
        