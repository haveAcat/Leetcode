nums=[1,3,5,6]
target=0

ss=0
result=0
for k in range(len(nums)):
    if nums[k]==target:
        return(k)
        ss+=1
if ss==0:
    for i in range(len(nums),0):
        if nums[i]<target:
            nums.insert[i,target]
            return(nums)
    
        
        
    
