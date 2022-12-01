# 2360. Longest Cycle in a Graph
# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

# Return the length of the longest cycle in the graph. If no cycle exists, return -1.

# A cycle is a path that starts and ends at the same node.

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        seen = [False]*n
        self.max_len = float('-inf')
        visiting = {}
        stack = []
        
        def dfs(i):
            if not seen[i]:
                if i in visiting:
                    # len stack-visiting[i] bc the stack could be multiple cycles
                    self.max_len = max(self.max_len, len(stack) - visiting[i])
                # if there is an outgoing edge
                elif edges[i] != -1:
                    # add length of current cycle to "visiting" dict
                    visiting[i] = len(stack)
                    stack.append(i)
                    # call dfs on the next node in the cycle
                    # which appends it to the stack and tracks curr len in visiting
                    dfs(edges[i])
                    # once wwe hit a cycle, pop all off stack
                    stack.pop()
                    # pop off visiting, its just meant to keep track of incides in the stack
                    visiting.pop(i)
                # mark as seen/visited
                seen[i] = True
                
        
        for i in range(n):            
            dfs(i)
        return self.max_len if self.max_len > 0 else -1  
