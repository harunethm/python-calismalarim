def openOrSenior(data):
    memberList = []
    for a in data:
        if(a[0] > 55 and a[1] > 7):
            memberList.append("Senior")
        else:    
            memberList.append("Open")
    return memberList

    

print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))
print(openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]))