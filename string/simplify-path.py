class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        print(path)
        for item in path:
            # go back, must have item to go back
            if stack and item == "..":
                stack.pop()
            # care .., since /../ = /
            elif item not in ["", ".",'..']: 
                stack.append(item)


        return "/" + "/".join(stack)