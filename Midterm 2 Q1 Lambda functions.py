# make the function gen_lambda(numbers, criteria) to return the lambda function to that takes a list of numbers based on the parameter number and criteria.
# The criteria is one of the following:
# “square”: return the lambda function that returns the square of each element
# “half” : return the lambda function that return the first half elements of the list(if odd number elements, N//2)
# “positive” : return the lambda function that return the positive elements in the list
# “negative”: return the lambda function that return the positive elements in the list
# Run Example
# returned_lambda = gen_lambda(10, "even")
# returned_lambda([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# it will return [2, 4, 6, 8, 10]


# square_lambda = gen_lambda(10, "positive")
# square_lambda([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# it will return [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# half_lambda = gen_lambda(10, "half")
# half_lambda([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# it will return [1, 2, 3, 4, 5]

def gen_lambda(numbers, criteria):
    if criteria == 'square':
        return lambda numbers: [i**2 for i in numbers]
    # elif criteria == 'even':  # didn't read directions clearly
    #     return lambda i: [i for i in numbers if i%2 == 0]
    elif criteria == 'half':
        return lambda numbers: numbers[:len(numbers)//2]  # apply index to the list of numbers
    elif criteria == 'positive':
        return lambda numbers: [i for i in numbers if i > 0]
    elif criteria == 'negative':
        return lambda numbers: [i for i in numbers if i < 0]


def main():
    square_lambda = gen_lambda(10, "square")
    result = square_lambda([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    half_lambda = gen_lambda(10, "half")
    result = half_lambda([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)  # [1, 2, 3, 4, 5]

    positive_lambda = gen_lambda(10, "positive")
    result = positive_lambda([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    negative_lambda = gen_lambda(10, "negative")
    result = negative_lambda([1, 2, 3, 4, -5, 6, -7, 8, -9, 10])
    print(result)  # [-5, -7, -9]


if __name__ == '__main__':
    main()
