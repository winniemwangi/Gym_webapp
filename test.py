def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]+nums[j]==target:
                return(j,i)       
    return()
print(twoSum(nums=[1,2,3,4,5], target=9))


# nums = [1,2,3,4,5]
# target = 5

# for i in range(len(nums)+1):
#     for j in range(i):
#       if nums[i]+nums[j]==target:
#         print(j,i)

# print()