a = int(input())
preklad = {1:'ABD', 2:'ACD', 3:'A'+5*'C'+'D'}
preklad2 = {4:'A'+preklad[2]+'D',5:'A'+preklad[3]+'C'+5*preklad[1]+'D'}
preklad6 = {6:'A'+preklad2[5]+'C'+5*'B'+5*preklad2[4]+'D'}
prklds = [preklad,preklad2,preklad6]
for prkld in prklds:
    if a in prkld.keys():
        print(prkld[a])
