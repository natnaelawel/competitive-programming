#%%
def maxDepth(s):
    mylist = list([])
    level = 0
    max_depth = 0
    for i in s:
        if i == "(":
            mylist.append("(")
            level += 1
        elif i == ")":
            mylist.pop()
            level -= 1
        max_depth = max(max_depth, len(mylist))
    if len(mylist) == 0:
        return max_depth 
    else: 
        return None
    

s = "(1+(2*3)+((8)/4))+1"
s = ""

print(maxDepth(s))
# %%
