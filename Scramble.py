class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        class ETree(object):        
            val = None
            left = None
            right = None
                
            def __init__(self, v):
                self.val = v                   
            
            def load(self):
                # Load the remainder of the tree
                v = self.val
                if len(v) > 1:
                    offset = len(v) // 2
                    self.left = ETree(v[0:offset]).load()
                    self.right = ETree(v[offset:]).load()
                return self
                                       
            def isequiv(self, t1, t2):
                v1 = t1.val
                v2 = t2.val
                if len(v1) != len(v2):
                    return False
                
                if t1 is None and t2 is None:
                    return True
                elif t1 is None and t2 is not None:
                    return False
                
                if len(v1) == 1:
                    return v1 == v2

                same = self.isequiv(t1.left, t2.left)  and self.isequiv(t1.right, t2.right)
                flip = self.isequiv(t1.left, t2.right) and self.isequiv(t1.right, t2.left)
                return same or flip
            
        if len(s1) != len(s2):
            return False
        
        if len(s1) == 0:
            return True
        
        if len(s1) == 1:
            return True if s1[0] == s2[0] else False
        
        t1 = ETree(s1).load()
        t2 = ETree(s2).load()
        return t1.isequiv(t1, t2)