test = [4, [1], 3]

def my_sort(element):
    if type(element) is list:
        return int(element[0])
    else:
        return element

def sort_it(lst: list):
    return sorted(lst, key=my_sort)

print(sort_it(test))