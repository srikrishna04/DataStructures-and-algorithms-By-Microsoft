test0 = {'input': {'arr': [2, 6, 4, 9, 1], 'target': 10}, 'output': (1, 3)}
test1 = {'input': {'arr': [2, 6, 4, 9, 1], 'target': 8}, 'output': (0, 2)}
test2 = {'input': {'arr': [2, 6, 4, 9, 5], 'target': 14}, 'output': (3, 5)}
test3 = {'input': {'arr': [3, 5, 2, 6, 4], 'target': 10}, 'output': (0, 3)}
test4 = {'input': {'arr': [3, 5, 2, 6, 4], 'target': 14}, 'output': (None, None)}
test5 = {'input': {'arr': [10], 'target': 10}, 'output': (0,1)}
test6 = {'input': {'arr':[], 'target':5}, 'output': (None, None)}
test7 = {'input':{'arr':[2, 3, 4, 0, 3, 4], 'target': 10}, 'output': (1, 5)}
tests = [test0, test1, test2, test3, test4, test5, test6, test7]

# def exam1(arr, target):
#     for i in range(len(arr)):
#         for j in range(i, len(arr)+1):
#             if sum(arr[i:j]) == target:
#                 return i, j
#     return None, None        
# for test in tests:
#     if exam1(**test['input']) == test['output']:
#         print(exam1(**test['input']) ,test['output'])


# def exam2(arr, target):
#     for i in range(len(arr)):
#         s = 0
#         for j in range(i, len(arr)+1):
#             if s == target:
#                 return i, j
#             elif s > target:
#                 break
#             if j < len(arr):
#                 s += arr[j]
#     return None, None 
# for test in tests:
#     if exam2(**test['input']) == test['output']:
#         print(exam2(**test['input']) ,test['output'])

# def exam3(arr, target):
#    i, j, sum = 0, 0, 0
#    while i < len(arr) and j < len(arr)+1:
#        if sum == target:
#            return i, j
#        elif sum < target:
#            if j < len(arr):
#                sum += arr[j]
#            j += 1
#        elif sum > target:
#            sum -= arr[i]
#            i += 1
#    return None, None 
# for test in tests:
#     if exam3(**test['input']) == test['output']:
#         print(exam3(**test['input']) ,test['output'])