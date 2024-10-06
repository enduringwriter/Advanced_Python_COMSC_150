# The tuple with the smallest gap should be the first one in the sorted list. If the gap is the same, then sort based on the first value in the tuple.
# Requirement
# Do NOT use sort() function. Develop your algorithms
# Return value : None. Use the same list in the Parameter
# Example 1: sort_list(numbers)
# Input: [(1, 5), (2, 3), (4, 8), (10, 12), (9, 10)]
# Output: [(2, 3), (9, 10), (10, 12), (1, 5), (4, 8)]

# Example 2:
# Input: [(5, 10), (3, 8), (1, 3), (7, 8), (2, 6)]
# Output: [(7, 8), (1, 3), (2, 6), (5, 10), (3, 8)]

def sort_list(numbers):
    length_of_tuple = len(numbers)
    
    for i in range(length_of_tuple):
        for x in range(0, length_of_tuple - i -1):
            gap_prior_tuple = abs(numbers[x][0] - numbers[x][1])
            gap_next_tuple = abs(numbers[x+1][0] - numbers[x+1][1])

            if gap_prior_tuple > gap_next_tuple:
                numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
            elif gap_prior_tuple == gap_next_tuple and gap_prior_tuple < gap_next_tuple:
                numbers[x+1], numbers[x] = numbers[x], numbers[x+1]
    
    numbers.sort(key=lambda x: (abs(x[0] - x[1])))


def main():
    numbers = [(1, 5), (2, 3), (4, 8), (10, 12), (9, 10)]
    sort_list(numbers)
    print(numbers)
    # it should print [(2, 3), (9, 10), (10, 12), (1, 5), (4, 8)]

    numbers = [(5, 10), (3, 8), (1, 3), (7, 8), (2, 6)]
    sort_list(numbers)
    print(numbers)
    # it should print [(7, 8), (1, 3), (2, 6), (5, 10), (3, 8)]


if __name__ == '__main__':
    main()
