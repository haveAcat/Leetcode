nums=[0,1,1,2,6,8,2]
val=2

k=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]=nums[i]
        k+=1
print(k)

    
