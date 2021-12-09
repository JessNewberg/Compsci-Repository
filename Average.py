def my_average(num_list):
    a = len(num_list)
    listsum = 0
    for x in num_list:
        listsum = listsum + x
    final = listsum/a
    return final
