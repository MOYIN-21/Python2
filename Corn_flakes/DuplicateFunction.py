def remove_duplicates(input_list):
    unique_elements = []
    encountered_elements = {}

    for _ in input_list:
        if _ not in encountered_elements:
            unique_elements.append(_)
            encountered_elements[_] = True

    return unique_elements


input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
result = remove_duplicates(input_list)
print(result)
