import random


def make_new_list(numbers, N):
    new_list = []
    for i in range(N):
        templist = numbers[i::N]  # every Nth value
        new_list.append(templist)
    return new_list

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    N = 3
    new_list = make_new_list(numbers, N)
    print('new_list : ', new_list)

    N = 5
    new_list = make_new_list(numbers, N)
    print('new_list : ', new_list)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    N = 2
    new_list = make_new_list(numbers, N)
    print('new_list : ', new_list)


if __name__ == '__main__':
    main()
