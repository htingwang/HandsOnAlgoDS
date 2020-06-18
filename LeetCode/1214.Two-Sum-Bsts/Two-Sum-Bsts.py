class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        stack = []
        s = set()
        while root1 or stack:
            while root1:
                stack.append(root1)
                root1 = root1.left
            root1 = stack.pop()
            s.add(target - root1.val)
            root1 = root1.right

        while root2 or stack:
            while root2:
                stack.append(root2)
                root2 = root2.left
            root2 = stack.pop()
            if root2.val in s: return True
            root2 = root2.right
        return False

