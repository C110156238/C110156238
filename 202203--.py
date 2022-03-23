grade=55
grade=grade+10

if grade>=60 and grade<=100:
    print("pass")
else:
    print("fall")


# ----------------------幸運數字----------------------------
y=2002
m=9
da=29

a=y//1000
b=(y-(a*1000))//100
c=(y-(a*1000)-100*b)//10
d=((y-(a*1000)-100*b)-10*c)

if (a+b+c+d+m+da//10+da%10) >=10:
    print((a+b+c+d+m+da//10+da%10)//10+(a+b+c+d+m+da//10+da%10)%10)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

sum=0
birthday="20020929"
for i in birthday:
    sum=sum+int(i)

if sum>=10:
    sum=sum//sum%10

if sum<=10:
    sum=sum//sum%10

print(sum)

print(list(range(1,11,1))) 

#1.................................................
for i in list(range(1,11,1)):
    print(i)
    sum=sum+i
print(sum)

#2.................................................
sum1 = 0
sum = 0
for i in list(range(1,11,2)):
    print(i)
    sum=sum+i
for j in list(range(2,11,2)):
    print(j)
    sum1=sum1+j
sum2=sum-sum1
print(sum2)

#3.................................................
sum3=0
for i in list(range(1,11,1)):
    if i%4 >1:
        sum3=sum3-i
    else:
        sum3=sum3+i
print(sum3) 

#4.................................................
sum4=0
for i in list(range(1,11,1)):
    if i%2 ==1:
        sum4+=1/i
    else:
        sum4-=1/i
print(sum4)

#5.................................................
sum5=0
for i in list(range(1,11,1)):
    if i==1:
        sum5+=i
    elif i%2 ==1:
        sum5+=(i-1)/i
    else:
        sum5-=(i-1)/i
print(sum5)

