class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        len_s = len(s)
        len_t = len(t)
        cnt = 0
        
        if len_s == 0:
            return True
        
        if len_s > len_t :
            return False
        
        for i in t:
            if i == s[cnt]:
                cnt += 1
        
            if cnt == len_s:
                return True
            
        return False
    
    