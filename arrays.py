"""
# WAP to search an element in the array. - Linear Search
#num = int(input("enter a number to search: "))
num = 45
arr = [12,23,45,65]

found = False

for i in range(len(arr)):
    # print(arr[i]) 
    if num == arr[i]:
        print("number found at index:",i)
        found = True
        break

if not found:
        print("number not found!") 
"""
"""
array = [10,20,30,22,79]
for i in range(len(array) -1 , 2,-1):
    print(array[i])
"""
"""
# WAP to insert an element in the array. 
array = [10,20,30,22,79]
num = 90
idx = 2
array.append(0)
print(array)

for i in range(len(array) - 1,idx,-1): 
    array[i] = array[i-1]

array[idx] = num
print("new array is: ",array) 
"""
"""
# WAP to delete an element from the array 
array = [10,23,34,56,67,88,99,90]
idx = 2
for i in range(idx,len(array)-1): 
    array[i] = array[i+1]
array.pop() # it is used to pop the last duplicate element of the array. 
print("new array is:", array)
"""
"""
# find average of the elements of the array 
array = [10,23,34,56,67,88,99,90]
sum = 0
for i in range(len(array)):
    sum = sum + array[i] 
avg = sum /len(array)
print("average of array is: ",avg)
"""
"""
# LEETCODE TWO SUM PROBLEM : 
nums = [2,7,11,15]
target = 9
seen = {} 
for i in range(len(nums)):
    number = target - nums[i]
    if number in seen:
        print(seen[number],i)
    seen[nums[i]] = i
"""

# LEETCODE MAXIMUM SUBARRAY PROBLEM.
nums = [-2,1,-3,4,-1,2,1,-5,4]
current_sum = 0
max_sum = nums[0]
for i in range(len(nums)):
    current_sum += nums[i]
    max_sum = max(max_sum,current_sum)
    if current_sum < 0:
        current_sum = 0
print(max_sum)

