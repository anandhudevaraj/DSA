"""
Self try of binary search
"""


def binary_search(input_array, item):
    low = 0
    high = len(input_array) - 1
    while True:
        mid = int((low + high) / 2)
        print("{} {} {} {}".format(input_array, low, high, mid))
        if input_array[mid] == item:
            return mid
        elif high == low:
            return -1
        elif item < input_array[mid]:
            high = mid
        else:
            low = mid + 1

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, 5))
