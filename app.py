def a(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (a(n-1)+a(n-2))
b=int(input())
print(a(b))