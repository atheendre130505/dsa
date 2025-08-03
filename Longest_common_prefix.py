class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

#check if individual letters of the smallest length str are available in every other str, if not continue, if they are then go to the next letter and check if that is also available in every other string, if not save whatever as the substr, if yes go to the next letter while appending the prev letter. 
        substr=""
        res = min(strs, key=len)
        for i in range(len(res)):
            for j in range(len(strs)):
                if strs[j][i]!=res[i]:
                    return substr
            substr+=res[i]
        
        return substr

                    


        

        