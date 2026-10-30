class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # using Kahn's Algo: BFS Topological Sort

        # initializing indegree array and setting it to zero
        indegree = [0] * numCourses

        # creating adjacency list
        adj = [[] for i in range(numCourses)]

        # counting indegrees & adding all crs -> pre in adj
        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
            
        # initializing empty queue for BFS
        q = deque()

        # appending crs with no pre in queue; i.e ones with indegee as zero
        for crs in range(numCourses):
            # append crs if no pre, i.e indegree as zero
            if indegree[crs] == 0:
                q.append(crs)

        # initializing finished course count as zero
        finish = 0

        # while loop for BFS
        while q:
            # getting nodes form queue
            node = q.popleft()
            
            # one node processed so increasing finish
            finish += 1

            # looping over adj list of nodes; adj[node]; nei == crs
            for nei in adj[node]:
                # removing edge from indegree
                indegree[nei] -= 1
                # append nei if no pre, i.e indegree as zero
                if indegree[nei] == 0:
                    q.append(nei)
        
        # this returns True if all courses can be finished, else False
        return finish == numCourses