# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # so wwe can have all left and all right (2n)
        # we can pull out as many pairs as n
        # 
        ret = []
        def backtrack(S = [], l = 0, r = 0):
            # if we've called it enough that we have n lists of parens
            # 2*n because one paren is two chars
            if len(S) == 2 * n:
                # make list of lists just one list
                ret.append("".join(S))
            # if we don't have n
            if l < n:
                # start by adding all the left brackets
                S.append("(")
                # call backtrack until wwe have n left brackets
                backtrack(S, l+1, r)
                # we call S.pop in the order we called backtrack in
                # this decreases the value of l bc of the stack
                # this restarts the call of backtrack bc l is < n again
                S.pop()
            # make a closing bracket as long as its paired wwith an open bracket
            if r < l:
                # then add all corresponding right brackets
                S.append(")")
                # call backtrack until wwe have l right brackets
                backtrack(S, l, r+1)
                # we call S.pop in the order we called backtrack in
                # this decreases the value of r bc of the stack
                S.pop()
        # initial call with no parens yet
        backtrack()
        return ret