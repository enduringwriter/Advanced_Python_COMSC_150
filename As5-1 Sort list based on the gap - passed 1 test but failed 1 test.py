import random
# code passed 1 test but failed the 2nd test
# code incomplete

"""
flowchart:
Initialize variable total as the length of numbers -> 
Loop over element from 0 to total - 1 -> 
For each element, loop over index from 0 to total - element - 1,
as the last element is sorted in the comparison -> 
Get tuple1x, tuple1y where x and y are the tuple set in form (x,y) using index
and do the same for tuple2x, tuple2y but using index + 1
for the next tuple in sequence -> 
Calculate gaps-> 
If gap_curr < gap_next, swap index values to compare the next tuple -> 
Return the sorted numbers
"""
def sort_tuples(numbers):
    total = len(numbers)
    for element in range(total):
        print(element)
        for index in range(total - element -1):
            print(index)
            
            tuple1x, tuple1y = numbers[index]
            print(tuple1x, tuple1y)
            tuple2x, tuple2y = numbers[index + 1]
            print(tuple2x, tuple2y)

            gap_curr = abs(tuple1x - tuple1y)
            gap_next = abs(tuple2x - tuple2y)

            if (gap_curr < gap_next):  # this causes an error: or (gap_curr == gap_next and tuple1x > tuple2x)
                print(f'tuple1x:{tuple1x}')
                temp = numbers[index]
                numbers[index] = numbers[index + 1]
                numbers[index + 1] = temp
    return numbers

def main():
    numbers = [(4, 1), (3, 2), (5, 0), (2, 3), (1, 4)]
    print('numbers before sort : ', numbers)
    sort_tuples(numbers)
    print('numbers after sort : ', numbers)

    numbers = [(1, 2), (3, 1), (5, 0), (1, -1), (7, 9),
               (3, 3), (2, 2), (1, 1), (2, 1), (1, 0)]
    print('numbers before sort : ', numbers)
    sort_tuples(numbers)
    print('numbers after sort : ', numbers)


if __name__ == '__main__':
    main()
