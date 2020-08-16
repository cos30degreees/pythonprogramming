from itertools import groupby
from operator import itemgetter
import itertools

val = [x for x in range(25)]


def find_pairs(values, target):
    pairs = []

    for num_one in values:
        for num_two in values:
            if num_one + num_two == target:
                pairs.append((num_one,num_two))
    if len(pairs) > 0:
        print('{} with target {}:  {}'.format(values, target, pairs))
    else:
        print('No Valid Pairs')

# print(find_pairs(val,22))


data = [ 1,2,3,4,5,6, 10, 15,16,17,18, 22,23,24,25,26,27,28]


keys = []
groups = []
sorted_data = sorted(data)
new_list = data[1:]
print(data)
new1 = []
print(new_list)
def split_list(n):

    new = [x  for x,y in zip(n,n[1:]) if y % x != 1]
    return new


indices = [x for x in split_list(data)]

consequtive = [x: y ]
consequtive = [x for x in data[0:] if x < ]
print(new_low)
print(new_high)
