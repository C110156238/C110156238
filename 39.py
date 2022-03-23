a = int(input("7"))

x = 1
while x <= a:
    y = 1
    n = abs(x-a//2-1)
    print(" " * n,end = "")
    print("*" * (a-2*n))
    x += 1
