tests = []
tests.append ({"input" : {'cards' : [10, 9, 7, 5, 1],'query' : 7},'output' : 2})
tests.append ({"input" : {'cards' : [10, 8, 6, 3, 1],'query' : 10},'output' : 0}) 
tests.append ({"input" : {'cards' : [10],'query' : 10},'output' : 0})
tests.append ({"input" : {'cards' : [10, 7, 6, 3, 2],'query' : 2},'output' : 4})
tests.append ({"input" : {'cards' : [ ],'query' : 10},'output' : -1})
tests.append ({"input" : {'cards' : [10, 5, 5, 3, 2],'query' : 3},'output' : 3})
tests.append ({"input" : {'cards' : [4,2, 1],'query' : 10},'output' : -1})
tests.append ({"input" : {'cards' : [10, 8, 8, 8, 1],'query' : 8},'output' : 1})


def binary_search(low, high, condition):
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid-1
        else:
            low = mid+1
    return -1
def first_position(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid>0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] > query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(cards)-1, condition) 
for test in tests:
    if first_position(**test['input']) == test['output']:
        print(first_position(**test['input']))

def last_position(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid>0 and cards[mid+1] == query:
                return 'right'
            else:
                return 'found'
        elif cards[mid] > query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(cards)-1, condition) 
for test in tests:
    if first_position(**test['input']) == test['output']:
        print(first_position(**test['input']))

