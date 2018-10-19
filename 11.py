height=[1,8,6,2,5,4,8,3,7]

#----------soultion1------------

result=0
v=0
for ii in range(len(height)):
    for jj in range(ii+1,len(height)):
        v=min(height[ii],height[jj])*(jj-ii)
        if v>result:
            result=v
print(result)


#----------soultion2------------

'''l=len(height)
        ans=0
        
        p1=0
        p2=l-1
        
        while p1<p2:
            
            ans=max(ans,min(height[p1],height[p2])*(p2-p1))
            
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        
        return ans
