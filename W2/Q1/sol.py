'''
    Author: Bhavya Budania
            131112089 (CSE-1)
'''

import math

# Function: ECLAT algorithm
def gen(cur_len, frqItemSet, min_sup):

    dct = dict()

    for akey in frqItemSet[cur_len].keys():

        for bkey in frqItemSet[cur_len].keys():

            if cmp(akey, bkey) == 0:
                continue

            if cur_len == 1:
                new_key = tuple(sorted((akey, bkey)))
            else:
                new_key = tuple(sorted(tuple(set(akey).union(bkey))))

            if len(new_key) == cur_len+1:

                if new_key in dct:
                    continue

                dct[new_key] = list(set(frqItemSet[cur_len][akey]).intersection(frqItemSet[cur_len][bkey]))


    frqItemSet[cur_len+1] = dict()

    for key in dct:
        if len(dct[key]) >= min_sup:
            frqItemSet[cur_len+1][key] = dct[key]


    if len(frqItemSet[cur_len+1]) > 0:
        gen(cur_len+1, frqItemSet, min_sup)
    else:
        return

# Function: Main Driver Function
def main():
    min_sup = int(raw_input('Enter minimum support: '))
    ntrans = int(raw_input('Enter no of transactions: '))
    fname  = raw_input('Enter file name: ')
    dct = dict()

    fhandle = open(fname, 'rb')
    i = 0

    for line in fhandle:
        item_lst = line.strip().split()

        print 'TID%d' % (i+1) , ' : ', item_lst
        
        if not len(item_lst) > 0:
            break

        for item in item_lst:
            if item not in dct:
                dct[item] = list()

            dct[item].append(i+1)

        i = i + 1


    frqItemSet = dict()
    cur_len = 1

    for key in dct:
        if len(dct[key]) >= min_sup:

            if cur_len not in frqItemSet:
                frqItemSet[cur_len] = dict()

            frqItemSet[cur_len][key] = dct[key]


    # We can apply ECLAT algorithm
    if len(frqItemSet[1]) > 0:
        gen(cur_len, frqItemSet, min_sup)

    for key in frqItemSet.keys():

        if len(frqItemSet[key]) == 0:
            break

        print 'Frequent-%d Itemsets: ' % key

        for item in frqItemSet[key].keys():
            print item , frqItemSet[key][item]

        print '\n'

if __name__ == '__main__':
    main()
