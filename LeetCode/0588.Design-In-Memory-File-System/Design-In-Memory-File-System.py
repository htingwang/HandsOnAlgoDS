class Folder(object):
    def __init__(self, name):
        self.name = name
        self.subdirs = []
        self.files = []
        
class File(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content
        
class FileSystem(object):

    def __init__(self):
        self.root = Folder("/")
        self.maps = {"/": self.root}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        cur = self.maps[path]
        if type(cur) == File:
            return [path.rsplit("/", 1)[1]]
        res = []
        for folder in cur.subdirs:
            res.append(folder.name.rsplit("/", 1)[1])
        for filename in cur.files:
            res.append(filename.name.rsplit("/", 1)[1])
        return sorted(res)

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        cur = path.split("/")
        pre = "/"
        cur_path = ""
        for name in cur[1:]:
            cur_path += "/" + name
            if cur_path not in self.maps:
                cur_folder = Folder(cur_path)
                self.maps[pre].subdirs.append(cur_folder)
                self.maps[cur_path] = cur_folder
            pre = cur_path
        #print(self.maps)

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        folder_s, filename_s = filePath.rsplit("/", 1)
        if folder_s == "": folder_s = "/"
        if filePath not in self.maps:
            folder = self.maps[folder_s]
            new_file = File(filePath, content)
            folder.files.append(new_file)
            self.maps[filePath] = new_file
        else:
            self.maps[filePath].content += content
            
    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.maps[filePath].content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
