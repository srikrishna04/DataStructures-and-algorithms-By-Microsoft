test0 = {'input' : {'seq1':'rabbit' , 'seq2':'raju' }, 'output' : 2}
test1 = {'input' : {'seq1': [1, 2, 4, 6, 9] , 'seq2': [1, 9, 2, 4, 5] }, 'output' : 3}
test2 = {'input': {'seq1': 'qwert', 'seq2': 'yuiop'}, 'output': 0}
test3 = {'input' : {'seq1':'condensed' , 'seq2':'dense' }, 'output' : 5}
test4 = {'input' : {'seq1':'' , 'seq2':'raju' }, 'output' : 0}
test5 = {'input' : {'seq1':'' , 'seq2':'' }, 'output' : 0}
test6 = {'input' : {'seq1':'abcdef', 'seq2': 'badcfe'}, 'output': 3}
tests = [test0, test1, test2, test3, test4, test5, test6]



def seq_dynprog(seq1, seq2):
    table = [[0 for _ in range(len(seq2) +1)] for _ in range(len(seq1)+1)]
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i+1][j], table[i][j+1])
    return table[-1][-1]
for test in tests:
    if seq_dynprog(**test['input']) == test['output']:
        print(test['output'])