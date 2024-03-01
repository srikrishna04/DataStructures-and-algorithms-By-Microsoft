# capacity >= sum of weights included and having max profit
# Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than capacity.



test0 = {'input': {'capacity':15 ,
                   'weights': [3, 4, 6, 1, 2, 8],
                   'profits': [9, 6, 2, 5, 3, 8]},
                   'output': 25}
# all included
test1 = {'input': {'capacity':15 ,
                   'weights': [3, 4 , 7, 1],
                   'profits': [9, 6, 2, 4]},
                   'output': 21}
# below capacity
test2 = {'input': {'capacity':5 ,
                   'weights': [3, 2, 5, 1],
                   'profits': [2, 3, 4, 9]},
                   'output': 12}
# none included
test3 = {'input': {'capacity':2 ,
                   'weights': [3, 4, 5],
                   'profits': [9, 6, 2]},
                   'output': 0}
tests = [ test0, test1, test2, test3]


def knap_memo(capacity, weights, profits):
    memo = { }
    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
        else:
            memo[key] = max(recurse(idx+1, remaining), profits[idx]+ recurse(idx+1, remaining-weights[idx]))
        return memo[key]
    return recurse(0, capacity)
for test in tests:
    if knap_memo(**test['input']) == test['output']:
        print(knap_memo(**test['input']), test['output'])