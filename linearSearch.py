# write description in own words
# def locate_cards(cards, query):
# pass

tests = []
tests.append ({"input" : {'cards' : [10, 9, 7, 5, 1],'query' : 7},'output' : 2})
tests.append ({"input" : {'cards' : [10, 8, 6, 3, 1],'query' : 10},'output' : 0}) 
tests.append ({"input" : {'cards' : [10],'query' : 10},'output' : 0})
tests.append ({"input" : {'cards' : [10, 7, 6, 3, 2],'query' : 2},'output' : 4})
tests.append ({"input" : {'cards' : [ ],'query' : 10},'output' : -1})
tests.append ({"input" : {'cards' : [10, 5, 5, 3, 2],'query' : 3},'output' : 3})
tests.append ({"input" : {'cards' : [4,2, 1],'query' : 10},'output' : -1})
tests.append ({"input" : {'cards' : [10, 8, 8, 8, 1],'query' : 8},'output' : 1})
print(tests)

def locate_cards(cards, query):
    position = 0
    print('cards: ', cards)
    print('query: ', query)
    while position < len(cards):
        print('position: ', position)
        if cards[position] == query:
            return position
        position += 1
    return -1

for test in tests:
    print(locate_cards(**test['input']) == test['output'])




    




