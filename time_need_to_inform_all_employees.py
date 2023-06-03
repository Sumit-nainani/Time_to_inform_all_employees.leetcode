# 
# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

# The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

# Return the number of minutes needed to inform all the employees about the urgent news.
# 


# approach:
#        do a dfs of every employee and take max time of each employee at same level.

class Solution:
    def dfs(self,s,adj,it) -> int:
        mx=0
        for child in adj[s]:
            mx=max(mx,self.dfs(child,adj,it))
        return mx+it[s]  

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        s=len(manager)
        adj=[[] for i in range(n+1)]
        for i in range(s):
            if(manager[i]==-1):
                continue
            adj[manager[i]].append(i)
        return self.dfs(headID,adj,informTime)
   