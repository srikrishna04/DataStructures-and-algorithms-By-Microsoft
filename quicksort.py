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

def quick_sort(nums, lo=0, hi= None):
    if hi is None:
        nums = list(nums)
        hi = len(nums)-1
    if lo < hi:
        pivot = partition(nums, lo, hi)
        quick_sort(nums, lo, pivot-1)
        quick_sort(nums, pivot+1, hi)
    return nums
def partition(nums, lo=0, hi=None):
    if hi is None:
        hi = len(nums) - 1
    l, r = lo, hi-1
    while l < r:
        if nums[l] <= nums[hi]:
            l += 1
        elif nums[r] > nums[hi]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    if nums[l] > nums[hi]:
        nums[l], nums[hi] = nums[hi], nums[l]
        return l
    else:
        return hi
print(quick_sort([1, 5, 3]))
for test in tests:
    if quick_sort(test['input']['nums']) == test['output']:
        print('before sorting' +" "+ str(test['input']['nums']))
        print('after sorting' +" "+ str(test['output']))