class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # and empty array for answers array
        ans = []

        # initializing hashmap for storing crs -> pre
        preMap = {i: [] for i in range(numCourses)}

        # adding all crs -> pre in preMap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # initializing empty visit Set, it will track visited courses
        visitSet = set()

        # initializing empty completed Set, it will avoid duplicate visited courses
        completedSet = set()

        # creating recursive dfs(crs)
        def dfs(crs):
            # checking base cases first

            # first: if crs in visit set, return False
            if crs in visitSet:
                return False
            
            # second: if crs in completed set, return True
            if crs in completedSet:
                return True

            # if not of any cases, add crs to visit set
            visitSet.add(crs)

            # looping pre in preMap and recursively checking using dfs
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # if no pre left,then remove crs from visit set
            visitSet.remove(crs)

            # if pre completed add it to completed set
            completedSet.add(crs)

            # then add the course to ans array 
            ans.append(crs)

            # then only return True when all completed
            return True

        # finally looping over all crs, then checking recursively via dfs
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return ans