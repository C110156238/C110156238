tmp=[60,70,35,55,90]
tmp1=[3,5,6,7,8]

tmp.append(50)
tmp1.append(60)
tmp.pop()
tmp.insert(2,60)
tmp.pop(2)
print(len(tmp))

kk=tmp.copy()
kk.append(55)
kk.reverse()
print(len(tmp1))
max=0
min=100
for i in range (len(tmp)):
    if tmp[i] > max:
        max = tmp[i]
    if tmp[i] < min:
        min = tmp[i]
print(max)
print(min)


tt=tmp.copy()
print()



g=0
h=[60,70,35,55,90]
for i in range(len(h)):
    if i < 4:
        if h [i] > h[i+1]:
            g=h[i] #存放
            h[i]=h[i+1] #替換
            h[i+1]=g #取代
print(h)

grades=[[96,65,73],[88,76,82],[92,84,89],[82,73,64],[70,83,68]]

for i in range(len(grades)):
    for j in range(len(grades[i])):
        print(grades[i][j],end=" ") #抓list[]的值
    print()

subtotal=0
for i in range(len(grades)):
    for j in range(len(grades[i])):
        subtotal=subtotal+grades[i][j]
    print(subtotal/3) #算出每個人的平均
    subtotal=0
print()

subtotal=0
for i in range(len(grades[0])): #找科目的分數
    for j in range(len(grades)): #找每個人的分數
        subtotal=subtotal+grades[j][i] #找到定位的數
    print(subtotal/5) #算出每科目的平均
    subtotal=0
print()

