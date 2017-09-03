import math
def quadratic(a,b,c):
    deta=b*b-(4*a*c)
    if deta<0:
        print('error')
    elif deta==0:
            x=-b/(2*a)
            return x
    if a==0 and b!=0:
        x=-(c/b)
        return x
    elif a==0 and b==0:
        x='error'
        return x
    else :
        x1=(-b+math.sqrt(deta))/(2 a)
        x2=(-b-math.sqrt(deta))/(2 a)
        return (x1,x2)
