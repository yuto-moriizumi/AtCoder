s=input()

while(True):
    if(s[:7]=="dreamer"):
        s=s[7:]
    elif(s[:6]=="eraser"):
        s=s[6:]
    elif(s[:5]=="dream" or s[:5]=="erase"):
        s=s[5:]
    elif(len(s)==0):
        print("YES")
        exit()
    else:
        print("NO")
        exit()