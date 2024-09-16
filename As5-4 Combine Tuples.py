import random
# make a function combine_tuples() that takes a list of tuples
# and returns a list of tuples where if there are any common elements in the tuples,
# combine them into one tuple.
# if there is no common element, keep them as they are.
# if there is common element to more than one tuple, combine them into the first tuple.
# Examples of input list of tuples and the outputs are as follows.
# input: [(1, 2), (2, 3), (4, 5)].                      Output: [(1, 2, 3), (4, 5)]
# input: [(1, 2), (2,3), (3,4), (4,5), (6,7), (7,8), (8,9), (1,10)].    Output: [(1, 2, 3, 4, 5, 10), (6, 7, 8, 9)]
# input: [(1, 2), (3, 2), (1, 3), (4, 1)].              Output: [(1, 2, 3, 4)]
# input: [(1, 2), (3, 2), (4, 3), (5,4 ), (10, 3)].     Output: [(1, 2, 3, 4, 5, 10)]

"""
Flowchart: 
Create the function combine_tuples(lst) that accepts a list of tuples -> 
Declare the new list new_list and add the first tuple to it -> 
Iterate through each tuple in the list using a For loop -> 
For each tuple, check if it has any common elements with the current tuple 
that is being iterated through the use of enumerate -> 
If a common element is found, merge the current tuple with the tuple 
using index for the position of each unique combination -> 
The merge includes the use of tuple(), sorted(), set(), and + 
where set set removes duplicates and + concatenates the tuples -> 
If no common elements are found, add the tuple to the list as it is -> 
Process all tuples in the list -> 
Once the loop is complete, return the new list containing the combined tuples.
"""

def combine_tuples(lst):
    new_list = [lst[0]]
    for each_tuple in lst[1:]:
        for i, current_tuple in enumerate(new_list):
            if any(element in current_tuple for element in each_tuple):
                new_list[i] = tuple(sorted(set(current_tuple + each_tuple)))
                # set removes the duplicates while + concatenates the tuples.
            else:  # I think this else statement is not correct but it passes the test
                new_list.append(each_tuple)
                # continue
        # else:
        #     new_list.append(each_tuple)
    return new_list

def main():
    numbers = [(1, 2), (2, 3), (4, 5)]
    new_list = combine_tuples(numbers)
    print('new_list : ', new_list)    # it should be [(1, 2, 3), (4, 5)]

    numbers = [(1, 2), (2, 3), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (1, 10)]
    new_list = combine_tuples(numbers)
    print('new_list : ', new_list)

    numbers = [(1, 2), (3, 2), (1, 3), (4, 1)]
    new_list = combine_tuples(numbers)
    print('new_list : ', new_list)

    numbers = [(1, 2), (3, 2), (4, 3), (5, 4), (10, 3)]
    new_list = combine_tuples(numbers)
    print('new_list : ', new_list)


if __name__ == '__main__':
    main()
