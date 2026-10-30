class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # creating hashmap for storing crs -> pre,, setting as [] first
        preMap = {i: [] for i in range(numCourses)}

        # making pairs [crs,pre] and adding it to preMap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # initializing empty visit set 
        visitSet = set()
        
        # creating a recursive dfs(crs)
        def dfs(crs):
            # checking the base cases

            # first: if pre left in visit set, return False
            if crs in visitSet:
                # cycle detected
                return False

            # second: if no pre left return True
            if preMap[crs] == []:
                return True

            # if not any case, then add it to visitSet
            visitSet.add(crs)

            # now looping recursively in preMap using dfs
            for pre in preMap[crs]:
                # if crs cannot be completed, return False
                if not dfs(pre):
                    return False
                
            # if it can be completed, remove from visit set
            visitSet.remove(crs)
            # then mark preMap[crs] = [] , as empty list as it can be completed
            preMap[crs] = []
            # then only, return True
            return True

        # finally looping over crs in all the numCourses
        for crs in range(numCourses):
            # again checking list, if any pre left, return False, else return True
            if not dfs(crs):
                return False
        return True