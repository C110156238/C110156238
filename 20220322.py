import random


tmp =[1,2,3,4,5]
tmp1 =(1,2,3)
print(tmp[1])
print(tmp[0])
tmp[2] = 4

grade= []
for i in range(1,56):
    grade.append(random.randint(0,100))

tmpk="C1101562"
id=[]
for i in range(1,55):
    id.append(tmpk+'{0:02d}'.format(i)) #加兩碼進學號裡


tmp2={"C110156201":40,"C110156202":43,"C110156203":100,"C110156238":60,"C11015233":20}
tmp4={"國文":90,"數學":90,"英文":60}
for i in range(1,10):
    tmp2.append(tmp4+'{0:03d}'.format(i))

print(tmp2['C110156202'])

tmp3={}
for i in range(1,54):
    tmp3[id[i]]=grade[i]