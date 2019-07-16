def generate_list_pair_set(first_list, second_list):
    return set(zip(first_list, second_list))

def run_test():
    firstList = [1, 2, 3, 4, 5]
    secondList = [10, 20, 30, 40, 50]
    print(generate_list_pair_set(firstList, secondList) == {(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)})

run_test()
