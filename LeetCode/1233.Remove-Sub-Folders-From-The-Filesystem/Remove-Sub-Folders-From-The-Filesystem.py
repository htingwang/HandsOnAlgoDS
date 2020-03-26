class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder_set = set(folder)
        res_set = set(folder)
        for f in folder:
            f_list = f.split("/")
            cur = ""
            for i in range(1, len(f_list) - 1):
                cur += "/" + f_list[i]
                if cur in folder_set:
                    res_set.remove(f)
                    break
        return list(res_set)
            
        
