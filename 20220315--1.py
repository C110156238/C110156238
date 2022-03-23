g=0
h=[60,70,35,55,90]
for j in range(len(h)):
    for i in range(len(h)-j-1):
             if h [i] > h[i+1]:
                g=h[i] #存放
                h[i]=h[i+1] #替換
                h[i+1]=g #取代
print(h)

