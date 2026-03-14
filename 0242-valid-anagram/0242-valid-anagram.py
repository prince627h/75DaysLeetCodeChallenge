class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # if len(s) != len(t):
        #     return False
        # elif not t.isalnum():
        #     return False
        # elif sorted(t) == sorted(s):
        #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False
        for idx in set(s):
            if s.count(idx) != t.count(idx):
                return False
        return True