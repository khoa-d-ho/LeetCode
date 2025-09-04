class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        invalid_names = ["", ".",'..']
        print(path)
        for item in path:
            # go back, must have item to go back
            if stack and item == "..":
                stack.pop()
            # care .., since /../ = /
            elif item not in invalid_names: 
                stack.append(item)


        return "/" + "/".join(stack)