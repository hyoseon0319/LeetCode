class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_one = {}
        dic_two = {}
        result = True
                
        if len(s) != len(t) :
            return False
        
        for s_v, t_v in zip(s, t):
            if s_v not in dic_one.keys():
                dic_one[s_v] = t_v

            else :
                if dic_one[s_v] != t_v:
                    result = False
                    break
                    
                        
        if result == True :
            for s_v, t_v in zip(s, t):
                if t_v not in dic_two.keys():
                    dic_two[t_v] = s_v
                
                else :
                    if dic_two[t_v] != s_v:
                        result = False
                        break

        return result
                