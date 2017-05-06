"""""
1,Nouns,1,Common Nouns,1,0.7
1,Nouns,1,Common Nouns,2,0.6
1,Nouns,2,Abstract Nouns,3,0.8
1,Nouns,3,Proper Nouns,4,0.2
1,Nouns,3,Proper Nouns,5,0.5
1,Nouns,3,Proper Nouns,6,0.4

2,Verbs,4,Action Verbs,7,0.9
2,Verbs,4,Action Verbs,8,0.1
2,Verbs,5,Transitive Verbs,9,0.3
2,Verbs,5,Transitive Verbs,10,0.6
2,Verbs,5,Transitive Verbs,11,0.4
2,Verbs,6,Reflexive Verbs,12,0.2
"""

import sys

def x(ques, num_q):
    num_q = int(num_q)
    if int(num_q) > len(ques):
        num_q = int(num_q) / len(ques)
        for q in ques:
            x(ques[q], num_q)
    else:
        for x in xrange(int(num_q)):
            if type(ques.get(ques.keys()[0])) is dict:
                #print ques.get(ques.keys()[0])
                num_q -= 1
                import ipdb; ipdb.set_trace()
                x(ques.get(ques.keys()[0]), num_q)
            else:
                print ques.get(ques.keys()[0])
                #counter -= 1

if len(sys.argv) > 1:
    num_q = sys.argv[1]
    #print num_q
    counter = num_q
    ques = {1: {1: {1: 0.7, 2: 0.6}, 2: {3: 0.8} , 3: {4: 0.2, 5: 0.5, 6: 0.4}},2: {4: {7: 0.9, 8: 0.1}, 5: {9: 0.3, 10: 0.6, 11:0.4}, 6: {12:0.2}}} 

    x(ques, num_q)
    










else:
    exit


    #