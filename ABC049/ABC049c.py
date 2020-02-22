import sys
sys.setrecursionlimit(20000)

s=input()
sl=len(s)

def ok(st):    
    stl=len(st)
    if(sl<=stl):
        if(s==st):
            return True
        else:
            return False
    
    if(s[:stl]==st):
        del stl
        return ok(st+"dream") or ok(st+"dreamer") or ok(st+"erase") or ok(st+"eraser")
    
    return False

if(ok("")):
    print("YES")
else:
    print("NO")