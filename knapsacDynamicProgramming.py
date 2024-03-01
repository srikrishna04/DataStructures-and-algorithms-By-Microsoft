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



def knap_dp(capacity, weights , profits):
    table = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for idx in range(len(weights)):
        for c in range(capacity+1):
            if weights[idx] > c:
                table[idx+1][c] = table[idx][c]
            else:
                table[idx+1][c] = max(table[idx][c], profits[idx] + table[idx][c-weights[idx]])
    return table[-1][-1]
for test in tests:
    if knap_dp(**test['input']) == test['output']:
        print(knap_dp(**test['input']), test['output'])