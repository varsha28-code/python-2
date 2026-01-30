# optimal 

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        left = 0 
        right = 0 
        maxLen = 0
        hashArray = [-1]*26 # S.C:- O(1) 
        while(right<n): # T.C :-  O(N) 
            # shrink 
            if(hashArray[ord(s[right])-ord('a')]!=-1 and hashArray[ord(s[right])-ord('a')]>=left):
                left = hashArray[ord(s[right])-ord('a')]+1 
            maxLen = max(maxLen,right-left+1)
            hashArray[ord(s[right])-ord('a')] = right
            right+=1 
        return maxLen 


better :- 

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        left = 0 
        right = 0 
        maxLen = 0
        d = {} # S.C :- O(N) 
        while(right<n): # T.C :-  O(N) 
            # shrink 
            if(s[right] in d and d[s[right]]>=left):
                left = d[s[right]]+1 
            maxLen = max(maxLen,right-left+1) 
            d[s[right]] = right
            right+=1 
        return maxL
