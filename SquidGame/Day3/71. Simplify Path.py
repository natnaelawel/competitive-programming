class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        out = []
        for sub in arr:
            if sub == ".." and len(out) > 0:
                out.pop()
            elif sub not in (".","",".."):
                out.append("/"+sub)
                
        return "".join(out) if len(out)>0 else "/"
        