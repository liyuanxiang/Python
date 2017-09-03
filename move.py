def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)#将a的前n-1盘子移动到b上
        move(1,a,b,c)#将a的最后一个盘子移动到c上
        move(n-1,b,a,c)#将b上的盘子移动到c上
    return None
    

