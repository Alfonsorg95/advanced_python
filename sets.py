def union(set1:set, set2:set):
    resulting_set = set1 | set2
    print(resulting_set)

def intersection(set1:set, set2:set):
    resulting_set = set1 & set2
    print(resulting_set)

def difference(set1:set, set2:set):
    resulting_set = set1 - set2
    print(resulting_set)

def symmetric_difference(set1:set, set2:set):
    resulting_set = set1 ^ set2
    print(resulting_set)

def run():
    my_set1 = {1, 2, 3, 4, 5}
    my_set2 = {4, 5, 6, 7, 8}
    union(my_set1, my_set2)
    intersection(my_set1, my_set2)
    difference(my_set1, my_set2)
    difference(my_set2, my_set1)
    symmetric_difference(my_set1, my_set2)

if __name__=='__main__':
    run()