test0 = {'input' : {'seq1':'rabbit' , 'seq2':'raju' }, 'output' : 2}
test1 = {'input' : {'seq1': [1, 2, 4, 6, 9] , 'seq2': [1, 9, 2, 4, 5] }, 'output' : 3}
test2 = {'input': {'seq1': 'qwert', 'seq2': 'yuiop'}, 'output': 0}
test3 = {'input' : {'seq1':'condensed' , 'seq2':'dense' }, 'output' : 5}
test4 = {'input' : {'seq1':'' , 'seq2':'raju' }, 'output' : 0}
test5 = {'input' : {'seq1':'' , 'seq2':'' }, 'output' : 0}
test6 = {'input' : {'seq1':'abcdef', 'seq2': 'badcfe'}, 'output': 3}
tests = [test0, test1, test2, test3, test4, test5, test6]

def lcs_recurse(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recurse(seq1, seq2, idx1+1, idx2+1)
    else:
        opt1 = lcs_recurse(seq1, seq2, idx1+1, idx2)
        opt2 = lcs_recurse(seq1, seq2, idx1, idx2+1)
        return max(opt1, opt2)
for test in tests:
    if lcs_recurse(**test['input']) == test['output']:
        print(test['output'])
