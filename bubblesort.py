test0 = {'input' : { 'nums' : [2, 5, 1, 7, 0, 6]},'output' : [0, 1, 2, 5, 6, 7]}
test1 = {'input' : { 'nums' : [2, 0,-1, 9, 4,-6]},'output' : [-6,-1, 0, 2, 4, 9]}
test2 = {'input' : { 'nums' : [1, 2, 3, 4, 5, 6]},'output' : [1, 2, 3, 4, 5, 6]}
test3 = {'input' : { 'nums' : [6, 5, 4, 3, 2, 1]},'output' : [1, 2, 3, 4, 5, 6]}
test4 = {'input' : { 'nums' : [2, 1, 1, 6, 3, 3]},'output' : [1, 1, 2, 3, 3, 6]}
test5 = {'input' : { 'nums' : []},'output' : []}
test6 = {'input' : { 'nums' : [2]},'output' : [2]}
test7 = {'input' : { 'nums' : [2, 2, 2, 2, 2, 2]},'output' : [2, 2, 2, 2, 2, 2]}
import random
in_list = list(range(100))
out_list = list(range(100))
random.shuffle(in_list)
test8 = {'input' : { 'nums' : [in_list]},'output' : [out_list]}
tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

def bubble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums
for test in tests:
    if bubble_sort(test['input']['nums']) == test['output']:
        print('before sorting' +" "+ str(test['input']['nums']))
        print('after sorting' +" "+ str(test['output']))

