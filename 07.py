x=int(input("input:"))
if x<0:
    """x=-1*x
    a=int(str(x)[::-1])
    a=-1*a"""
    a=-1*int(str(-x)[::-1])
else:
    a=int(str(x)[::-1])
    """if str(a)[0]==0:
        del str(a)[0]"""
if (x>(2**32/2-1) or x<(-(2**32/2))):
    a=0            
print(a)
    
