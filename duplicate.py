nums = [1, 2, 3, 2, 4, 5, 1,3]
dup=[]
rest=[]
# for i in nums:
#     if nums.count(i) > 1 and i not in dup:
#         dup.append(i)
# print(dup)

for i in nums:
    if i not in rest:
        rest.append(i)
    else:
        dup.append(i)
print(dup)