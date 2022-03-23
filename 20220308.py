# ----------------------UNICODE(2 BYTE) aka. ASCII CODE(1 BYTE)----------------------------
from ast import For


tmp="國立高雄科技大學劉宇哲"
for i in tmp:
    print(hex(ord(i)))

# ----------------------A/B/D/G/K/P ASCII CODE(chr轉回)----------------------------
sum = 65
for j in range(0,6,1):
    sum += j
    print(chr(sum))

# ----------------------1----------------------------
for i in range(1,6,1):
    sum=""
    for j in range(0,i,1):
        sum += "*"
    print(sum)
# ----------------------1.5----------------------------
for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print()
# ----------------------2----------------------------
for i in range(1,6,1):
    sum=""
    for j in range(5,i,-1):
        sum += "o"
    for j in range(0,i,1):
        sum += "x"
    print(sum)
# ----------------------3----------------------------
for i in range(1,6,1):
    sum=""
    for j in range(5,i,-1):
        sum += " "
    for j in range(0,i,1):
        sum += "x"
    for j in range(0,i-1,1):
        sum += "x"
    print(sum)
# ----------------------4----------------------------
for i in range(1,6,1):
    sum=""
    for j in range(5,i,-1):
        sum += " "
    for j in range(0,1,1):
        sum += "x"
    if i > 1:
        for j in range(0,1,1):
            sum += " "
    if i > 1:
        for j in range(0,1,1):
            sum += "x"
    if i > 2:
        for j in range(0,1,1):
            sum += " "
    if i > 2:
        for j in range(0,1,1):
            sum += "x"
    if i > 3:
        for j in range(0,1,1):
            sum += " "
    if i > 3:
        for j in range(0,1,1):
            sum += "x"
    if i > 4:
        for j in range(0,1,1):
            sum += " "
    if i > 4:
        for j in range(0,1,1):
            sum += "x"
    print(sum)
# ----------------------5----------------------------
for i in range(5): #每回圈一次會使i+1 一旦i=5(在執行前檢查)就部會不執行內容直接結束迴圈
    for j in range(4-i): #每回圈一次會使j+1 一旦j=4-i(因為越前面的排數要輸入的空格越多)結束迴圈 結束後j重製 
        print(" ",end="") #每回圈會多一次輸入空格
    for j in range(2*i+1): #每回圈一次會使j+1 一旦j=4-i(空格後須輸入的數相等於當前行數的兩倍+1)直接結束迴圈
        if j%2 >0: #判斷後面需輸入的是空格還是x 一旦j%2>0(也就是j等於奇數) 就會輸入空格
            print(" ",end="")                                       #(由於起始J為0 因此會被判斷為偶數)
        else:
            print("x",end="")
    print()
for i in range(4,0,-1):#因為空格數要從低到高因此要讓迴圈反著運行
    for j in range(4-(i-1)):#每回圈一次會使j+1 一旦j=4-(i-1)(因為第一行就會需要空格因此要-1)
        print(" ",end="")#每回圈一次會多輸入1個空格
    for j in range(2*i):#每回圈一次會使j+1 一旦j=2*1(因為如果條件跟上面的一樣會多一個x)
        if j % 2 > 0:                                               #(因為I()行數的起始數不再為0 不需考慮0的情況)
            print(" ",end="")
        else:   
            print("x",end="")
    print()
#----------------------6-----------------------------
for i in range(5): 
    for j in range(i): 
        print("x",end="")  
    for j in range(10-2*i): 
        print(" ",end="")    
    for j in range(i): 
        print("x",end="")                                    
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("x",end="")
    for j in range(10-2*i):                                           
        print(" ",end="")
    for j in range(i): 
        print("x",end="")  
        
    print()
# ----------------------AB---------------------------
que=str("5683")
ans=str("1658")
A = 0
B = 0
for i in range(4):
    for j in range(4):
        if que[i]==ans[j]:
            if i == j:
                A += 1
            else:
                B += 1
print("A=",A,"B=",B)



 




