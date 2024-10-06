# Make the function transform(numbers ) that takes a list of numbers and returns the transformed list.
# Return value
# New list
# Call example
# newlist = transform(numbers)


# Assume that all the inner lists are of the same length.
# Example:
# Input list : [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# Output list : [ [1, 4, 7], [2, 5, 8], [3, 6, 9] ]
# Example 2:
# Input list : [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12] ]
# Output list : [ [1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12] ]
# Example 3:
# Input list : [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ]
# Output list : [ [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16] ]

def transform(numbers):
    new_list = []

    # assumption that each is sublist is the same
    length = len(numbers[0])
    
    for i in range(length):
        sublist = [sublist[i] for sublist in numbers]
        new_list.append(sublist)
    return new_list

def main():
    numbers = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transform(numbers))
    # it should print [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    numbers = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    print(transform(numbers))
    # it should print [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]

    numbers = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(transform(numbers))
    # it should print [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]


if __name__ == '__main__':
    main()
