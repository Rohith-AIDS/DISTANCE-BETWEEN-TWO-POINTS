a=int(input())
b=int(input())
c=int(input())
if a>b:
    print(a,"is greater than",b,"and",c)
    elif b>a:
        print(b,"is greater than",a,"and",c)
    if a>c:
        print(a,"is greater than",c,"and",b)
        elif c>a:
            print(c,"is greater than",a,"and",b)
else:
    print("Three numbers are equal")